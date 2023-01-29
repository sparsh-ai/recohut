from airflow.hooks.postgres_hook import PostgresHook
from airflow.hooks.http_hook import HttpHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

from helpers import SqlQueries

import datetime as dt
import re

class StageGithubJobsOperator(BaseOperator):

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 # conn_id = your-connection-name
                 pgsql_conn_id,
                 http_conn_id,
                 max_pages=10,
                 *args, **kwargs):

        super(StageGithubJobsOperator, self).__init__(*args, **kwargs)

        self.pgsql_conn_id = pgsql_conn_id
        self.http_conn_id = http_conn_id
        self.max_pages = max_pages

    def execute(self, context):
        pgsql = PostgresHook(postgres_conn_id=self.pgsql_conn_id)
        http = HttpHook(http_conn_id=self.http_conn_id, method='GET')

        self.log.info("Will recreate the table staging_github_jobs...")
        pgsql.run(SqlQueries.recreate_staging_github_jobs_table)

        params = {'page': 1}
        endpoint = '/positions.json'
        pages_count = 1
        self.log.info(f"Will request GitHub Jobs API (page: {params['page']})...")
        response = http.run(endpoint, params)
        results = response.json()
        self.insert_results_on_staging(pgsql, results)

        while len(results) > 0 and params['page'] <= self.max_pages:
            params['page'] = params['page'] + 1
            self.log.info(f"Will request GitHub Jobs API (page: {params['page']})...")
            response = http.run(endpoint, params)
            results = response.json()
            self.insert_results_on_staging(pgsql, results)
            pages_count = pages_count + 1

        self.log.info(f"Done fetching the {pages_count}/{self.max_pages} pages in total.")

    def insert_results_on_staging(self, pgsql, results):
        results_len = len(results)

        self.log.info(f"Will insert the results on the staging_github_jobs table (results length: {results_len})...")

        if results_len <= 0:
            self.log.info("No results to insert.")
            return

        for result in results:
            result['created_at'] = (
                dt.datetime.strptime(result['created_at'], "%a %b %d %H:%M:%S %Z %Y")
                           .strftime("%Y-%m-%d %H:%M:%S")
            )
            # clean utf8 with more than 4 bytes
            re_pattern = re.compile(u'[^\u0000-\u07FF\uE000-\uFFFF]', re.UNICODE)
            result['title'] = re_pattern.sub(u'\uFFFD', result['title'])
            result['description'] = re_pattern.sub(u'\uFFFD', result['description'])
            values = [v for v in result.values()]
            pgsql.run(SqlQueries.insert_into_staging_github_jobs_table, parameters=values)
        self.log.info("Done!")
