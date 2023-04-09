from asyncio import create_subprocess_shell
import json
import logging
from turtle import update
import requests as rq
import json
import pandas as pd
import os
from jinja2 import Template

from packages.config import Config
from packages.redshift_resource import Redshift

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SmartSheet:
    def __init__(self):
        config = Config('config/config.yaml').getConfigObject()

        self.bucket = config['Resources']['s3']['bucket']
        self.smart_sheet = config['Resources']['smart_sheet']
        rs_config = config['Resources']['redshift']
        self.rs = Redshift(
                user=rs_config['user'],
                password=rs_config['password'],
                host=rs_config['host'],
                port=rs_config['port'],
                database=rs_config['database']
            )

        self.base_url = "https://api.smartsheet.com/2.0/"
        self.header = {
            "Authorization": "Bearer " + self.smart_sheet['access_token'],
            "Content-Type": "application/json"
        }

    def pull_sheet_id(self, schema_name, table_name):
        """
        Need to account for different schemas
        """
        if schema_name == 'shopify':
            table_name = 'shopify_' + table_name

        sheet_id_key = table_name + "_id"
        sheet_id = self.smart_sheet[sheet_id_key]

        return sheet_id

    def pull_sheet_data(self, sheet_id):
        all_data = self.header
        all_data['includeAll'] = "true"

        sheet = rq.get(
            self.base_url + 'sheets/' + sheet_id,
            headers=all_data
        )
        sheet_data = json.loads(sheet.content)

        column_to_id_map = {}
        columns = sheet_data['columns']
        for c in columns:
            column_to_id_map[c["title"]] = c["id"]

        if sheet_data['totalRowCount'] > 0:
            last_modified = sheet_data['modifiedAt']
        else:
            last_modified = "2019-01-01"
        rows = sheet_data['rows']

        return column_to_id_map, last_modified, rows

    def gen_query(self, schema_name, table_name, last_modified_ts):
        query_path = os.path.join('smartsheet_templates',schema_name, (table_name + '.sql'))
        with open(query_path, 'r') as sql_query:
            query_text = sql_query.read()

        query = Template(query_text).render(last_modified_at=last_modified_ts)

        return query

    def pull_dw(self, schema_name, table_name, last_modified_ts):
        query = self.gen_query(schema_name, table_name, last_modified_ts)
        rs_df = pd.read_sql(query, self.rs.engine)
        
        logger.info(f"Pulled {rs_df.shape[0]} rows for Smart Sheet Update")

        return rs_df

    def df_to_cells(self, rs_df, column_to_id_map, update=False):
        logger.info(f"Converting DF to row objects for Smart Sheet Update")
        rows_to_add = []
        for row in rs_df.iterrows():
            cells = []
            for col in row[1].index:
                if col in column_to_id_map.keys():
                    cell = {
                        "columnId": column_to_id_map[col],
                        "value":row[1][col],
                    }
                    cells.append(cell)

            if update:
                cell_row = {
                    "id":row[1]['row_id'],
                    "cells": cells
                }

            else:
                cell_row = {
                    "toBottom":"true",
                    "cells": cells
                }

            rows_to_add.append(cell_row)

        return json.dumps(rows_to_add)

    def find_updates(self, rs_df, rows, column_to_id_map, pk):
        """
        Compares the postgres table to sheet to find updates or new items. Since all postgres rows will be pulled after last_modified date
        we just need to look at a set intersection with the primary keys.
        The intersection == rows to update. The difference == rows to add new
        """
        updates = {}

        rs_update_set = set(rs_df[pk].unique())
        rows_pk_col_id = column_to_id_map[pk]

        # TODO this seems expensive and not scalable. Ideally we use the search sheet feature but were dealing with an unauthorized bs
        for row in rows:
            for cell in row['cells']:
                if cell['columnId'] == rows_pk_col_id:
                    if cell['value'] in rs_update_set:
                        updates[cell['value']] = row['id']
                    break

        rs_df['row_id'] = rs_df[pk].map(updates)
        new_rows_df = rs_df.loc[rs_df['row_id'].isna()]
        update_rows_df = rs_df.loc[~rs_df['row_id'].isna()]

        return new_rows_df, update_rows_df

    # TODO get authorized to search sheets for ids
    def smart_sheet_id_map(self, sheet_id):
        """
        If a rows is updated, we need to identify that record in the corresponding Smart Sheet.
        """

        pass

    def add_rows(self, schema_name, table_name, pk, last_update = None):
        """
        Insert new rows into a Smart Sheet spreadsheet. Finds
        """
        sheet_id = self.pull_sheet_id(schema_name, table_name)
        column_to_id_map, last_modified, rows = self.pull_sheet_data(sheet_id)
        last_modified = last_modified if not last_update else last_update

        rs_df = self.pull_dw(schema_name, table_name, last_modified)
        new_rows, rows_to_update = self.find_updates(rs_df, rows, column_to_id_map, pk)

        if new_rows.shape[0] > 0: 
            logger.info(f"Adding {new_rows.shape[0]} new rows")
            new_cells = self.df_to_cells(new_rows, column_to_id_map)
            new_results = rq.post(
                url = self.base_url + "sheets/" + sheet_id + "/rows",
                headers=self.header,
                data=new_cells
            )
            new_results.raise_for_status()

        if rows_to_update.shape[0] > 0:
            logger.info(f"Updating {rows_to_update.shape[0]} rows")
            update_cells = self.df_to_cells(rows_to_update, column_to_id_map, update=True)
            update_results = rq.put(
                url = self.base_url + "sheets/" + sheet_id + "/rows",
                headers=self.header,
                data=update_cells
            )
            update_results.raise_for_status()

        return None


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--schema_name", "-sn", required=True, help="Schema Name")
    parser.add_argument("--table_name", "-tb", required=True, help="Table name")
    parser.add_argument("--primary_key", "-pk", required=True, help="PK of Table we need to compare to smart sheet data")
    parser.add_argument("--last_update", "-lu", help="Can use an arbitrary last update date to get fields")

    args = parser.parse_args()

    sse = SmartSheet()
    sse.add_rows(args.schema_name, args.table_name, args.primary_key, args.last_update)