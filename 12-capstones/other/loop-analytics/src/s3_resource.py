import csv
import gzip
import os
import boto3
import logging
import uuid

from io import StringIO, BytesIO

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class S3:
    def __init__(self, bucket, chunk_size=10000):
        self.client = boto3.client('s3')
        self.bucket = bucket
        self.chunk_size = chunk_size

    def upload_file(self, local_path, s3_path):
        logger.info('uploading {} to {}'.format(local_path, s3_path))
        self.client.upload_file(local_path, self.bucket, s3_path)
        os.remove(local_path)

    def upload_gz_buffer(self, gz_buffer, s3_path):
        logger.info('uploading a buffer to {}'.format(s3_path))
        self.client.put_object(Bucket=self.bucket, Key=s3_path, Body=gz_buffer.getvalue())

    def upload_df(self, df, s3_path):
        csv_buffer = StringIO()
        df.to_csv(csv_buffer, header=False, index=False)

        csv_buffer.seek(0)
        gz_buffer = BytesIO()

        # compress string stream using gzip
        with gzip.GzipFile(mode='w', fileobj=gz_buffer) as gz_file:
            gz_file.write(bytes(csv_buffer.getvalue(), 'utf-8'))

        self.upload_gz_buffer(gz_buffer, s3_path)

    def upload_lol(self, lol, s3_path):
        csv_buffer = StringIO()
        writer = csv.writer(csv_buffer, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerows(lol)

        csv_buffer.seek(0)
        gz_buffer = BytesIO()

        # compress string stream using gzip
        with gzip.GzipFile(mode='w', fileobj=gz_buffer) as gz_file:
            gz_file.write(bytes(csv_buffer.getvalue(), 'utf-8'))

        self.upload_gz_buffer(gz_buffer, s3_path)

    def stream_writer(self, data, s3_dest_path):
        logger.info('writing data to s3..')
        tmp_file_name = '{}.csv'.format(uuid.uuid4())
        f = gzip.open(tmp_file_name, 'wt')
        writer = csv.writer(f)

        i = 0
        part_ct = 1
        for row in data:
            i += 1
            writer.writerow(row)
            if i % self.chunk_size == 0:
                f.close()
                file_name = '/part-{}.gz'.format(str(part_ct).zfill(5))
                self.upload_file(tmp_file_name, s3_dest_path + file_name)
                part_ct += 1
                f = gzip.open(tmp_file_name, 'wt')
                writer = csv.writer(f)

        f.close()
        file_suffix = '/part-{}.gz'.format(str(part_ct).zfill(5))
        self.upload_file(tmp_file_name, s3_dest_path + file_suffix)

    def stream_dict_writer(self, data, fieldnames, s3_dest_path):
        tmp_file_name = '{}.csv'.format(uuid.uuid4())
        f = gzip.open(tmp_file_name, 'wt', encoding='utf-8')
        writer = csv.DictWriter(f, fieldnames)

        i = 0
        part_ct = 1
        for row in data:
            i += 1
            writer.writerow(row)
            if i % self.chunk_size == 0:
                f.close()
                file_name = '/part-{}.gz'.format(str(part_ct).zfill(5))
                self.upload_file(tmp_file_name, s3_dest_path + file_name)
                part_ct += 1
                f = gzip.open(tmp_file_name, 'wt')
                writer = csv.DictWriter(f, fieldnames)

        f.close()
        file_suffix = '/part-{}.gz'.format(str(part_ct).zfill(5))
        self.upload_file(tmp_file_name, s3_dest_path + file_suffix)
