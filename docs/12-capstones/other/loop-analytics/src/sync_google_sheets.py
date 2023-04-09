import os
import sys
import logging
import gspread
import datetime
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

from packages.s3_resource import S3
from packages.redshift_resource import Redshift
from packages.schema import Schema
from packages.config import Config

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class GoogleSheetsDev:
    def __init__(self):
        SCOPES = ['https://spreadsheets.google.com/feeds',
            'https://www.googleapis.com/auth/drive',
            'https://www.googleapis.com/auth/spreadsheets']
        config = Config('config/config.yaml').getConfigObject()
        google_config = config['Resources']['googlesheets']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(google_config['key_file_path'], SCOPES)
        self.client = gspread.authorize(credentials)

        self.schema = Schema('googlesheets')

        self.bucket = config['Resources']['s3']['bucket']
        self.s3_prefix = google_config['s3_prefix']

        rs_config = config['Resources']['redshift']
        self.rs = Redshift(
                user=rs_config['user'],
                password=rs_config['password'],
                host=rs_config['host'],
                port=rs_config['port'],
                database=rs_config['database']
            )

    def extract_sheets(self, workbook_name, sheet_name, table_name):
        wks = self.client.open(workbook_name)
        if not sheet_name:
            sheets = [sheet for sheet in wks.worksheets()]
        else:
            sheets = [wks.worksheet(sheet_name)]
        rows = []
        for sheet in sheets:
            logger.info("Extracting sheet {} from workbook {}".format(sheet, workbook_name))

            if (sheet.title == table_name) | (sheet.title=='DW_upload') | (sheet.title == 'NEW_FINAL'):
                rows.extend(sheet.get_all_values()[1:])

            if sheet_name in ["Loop Master", "Purchase Master"]:
                rows.extend(sheet.get_all_values()[3:])
                rows = [r for r in rows if (r[0] != 'Add new lines after 5/1 above this line') and (r[0] != 'Add items after 5/1 above this line')]

            if sheet_name == 'FB Ad Key':
                rows.extend(sheet.get_all_values()[1:])
                rows = [[r[10], r[11], r[12]] for r in rows]

        return rows

    def load_data(self, data, table_name):
        extract_ts = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        out_prefix = '{}/{}'.format(self.s3_prefix, extract_ts)
        s3 = S3(self.bucket)
        s3.stream_writer(data, out_prefix)

        s3_path = 's3://{}/{}/part'.format(self.bucket, out_prefix)

        self.rs.loadToStagingTable(self.schema, table_name, s3_path)  # do this to make sure this load works
        self.rs.dropTable(self.schema, table_name)
        self.rs.createTable(self.schema, table_name)
        self.rs.load(self.schema.name, table_name, s3_path)

    def create_gs_table(self, table_name):
        self.rs.createSchema(self.schema)
        self.rs.createTable(self.schema, table_name)

    def reshape_retention_data(self, data):
        # find relevant data - look for "Existing customers engagement" in column b, and assume line break after that table
        start_index = None
        end_index = None
        for i in range(len(data)):
            if data[i][1] == 'Existing customers engagement':
                start_index = i
            elif start_index and data[i][1] == '':
                end_index = i
                break

        filtered_data = data[start_index: end_index]

        # reshape
        df = pd.DataFrame(filtered_data)
        df.columns = df.iloc[0]
        df.drop(df.index[0], inplace=True)
        long  = df.melt(id_vars=['','Existing customers engagement'])
        long.columns = ['cohort_size', 'cohort_month', 'month', 'engagement_pct']
        long['cohort_size'] = long['cohort_size'].astype(float)
        long['cohort_month'] = pd.to_datetime(long['cohort_month'])
        long['month'] = pd.to_datetime(long['month'])
        long['engagement_pct'] = long['engagement_pct'].apply(lambda x: x.replace('%', '')).replace('', '0.0')
        long['engagement_pct'] = long['engagement_pct'].astype(float) / 100.0
        long['expected_clients'] = long['cohort_size'] * long['engagement_pct']

        return long.values.tolist()

    def extract_and_load(self, workbook_name, sheet_name, table_name):
        data = self.extract_sheets(workbook_name, sheet_name, table_name)
        # ad hoc reshaping
        if workbook_name == 'Curbee Financial Model':
            data = self.reshape_retention_data(data)
        self.create_gs_table(table_name)
        self.load_data(data, table_name)

    def pull_redshift(self, schema_name, table_name, order_by, where_clause):
        df = self.rs.table_to_df(schema_name, table_name, order_by, where_clause)

        return df

    def write_to_sheet(self, df, workbook_name, worksheet_name):
        """
        This writes a DF to the designated workbook/sheet in google sheets
        """
        rows, cols = df.shape
        
        logger.info(f"Writing {df.shape[0]} rows to sheet {worksheet_name} in workbook {workbook_name}")

        try:
            wkb = self.client.open(workbook_name)

            try:
                wks = wkb.worksheet(sheet_name)
                logger.info(f"Clearing {worksheet_name} in workbook {workbook_name}")
                wks.clear()
                assert len (wks.get_all_records()) == 0

            except gspread.exceptions.WorksheetNotFound:
                logger.info(f"Worksheet: {worksheet_name} not in workbook...creating {worksheet_name} in {workbook_name}")
                wks = wkb.add_worksheet(title=worksheet_name, rows=rows, cols=cols)


        except gspread.exceptions.SpreadsheetNotFound:
            logger.info(f"Workbook: {workbook_name} not found...creating {worksheet_name} in {workbook_name}")
            wkb = self.client.create(workbook_name)
            wks = wkb.add_worksheet(title=worksheet_name, rows=rows, cols=cols)

        df = df.astype(str)  # stringly typed to load into spreadsheet to avoid seralization issues
        wks.update([df.columns.values.tolist()] + df.values.tolist())
        assert len (wks.get_all_records()) > 0


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--workbook", "-wb", help="Workbook Name")
    parser.add_argument("--sheet_name", "-sh", help="Workbook Sheet name")
    parser.add_argument("--table_name", "-tb", help="DB Table Name")
    parser.add_argument("--upload", "-up",  action="store_true",  help="Upload Google sheet to DB")
    parser.add_argument("--download", "-dn",  action="store_true",  help="Download DB to google sheets")
    parser.add_argument("--schema_name", "-sc", help="DB Schema Name")
    parser.add_argument("--order_by", "-o", nargs='+', default=[], help="Order the pulled table by")
    parser.add_argument("--where_clause", "-wc", default="", help="A SQL where clause to inject")

    args = parser.parse_args()

    if not (args.upload | args.download):
        raise ValueError('Must have download or upload argument specified')

    if args.upload:
        workbook_name = args.workbook
        table_name = args.table_name
        sheet_name = args.sheet_name if args.sheet_name else None
        gse = GoogleSheetsDev()
        gse.extract_and_load(workbook_name, sheet_name, table_name)

    if args.download:
        workbook_name = args.workbook
        sheet_name = args.sheet_name
        table_name = args.table_name
        schema_name = args.schema_name
        order_by = args.order_by
        where_clause = args.where_clause
        gse = GoogleSheetsDev()
        df = gse.pull_redshift(schema_name, table_name, order_by, where_clause)
        gse.write_to_sheet(df, workbook_name, sheet_name)

