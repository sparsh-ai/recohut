from airflow.hooks.postgres_hook import PostgresHook
from airflow.hooks.http_hook import HttpHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

from helpers import SqlQueries

import feedparser
from datetime import datetime
from time import mktime


class StageStackoverflowJobsOperator(BaseOperator):

    @apply_defaults
    def __init__(self,
                 # Define your operators params (with defaults) here
                 # Example:
                 # conn_id = your-connection-name
                 pgsql_conn_id,
                 http_conn_id,
                 *args, **kwargs):

        super(StageStackoverflowJobsOperator, self).__init__(*args, **kwargs)

        self.pgsql_conn_id = pgsql_conn_id
        self.http_conn_id = http_conn_id

    def execute(self, context):
        pgsql = PostgresHook(postgres_conn_id=self.pgsql_conn_id)
        http = HttpHook(http_conn_id=self.http_conn_id, method='GET')

        self.log.info("Will recreate the table staging_stackoverflow_jobs...")
        pgsql.run(SqlQueries.recreate_staging_stackoverflow_jobs_table)

        endpoint = '/jobs/feed'
        self.log.info(f"Will request Stackoverflow RSS Feed...")
        response = http.run(endpoint)
        feed = feedparser.parse(response.text)
        results = feed.entries
        results_len = len(results)
        inserted_results = self.insert_results_on_staging(pgsql, results)

        self.log.info(f"Done fetching the {inserted_results}/{results_len} registries in total.")

    def insert_results_on_staging(self, pgsql, results):
        results_len = len(results)

        self.log.info(f"Will insert the results on the staging_stackoverflow_jobs table (results length: {results_len})...")

        if results_len <= 0:
            self.log.info("No results to insert.")
            return 0

        for post in results:
            registry = [
                post.id, # 'id':
                post.link, # 'remote_url':
                post.location if 'location' in post else None, # 'location':
                post.author, # 'company_name':
                post.title, # 'title':
                post.summary, # 'description':
                ",".join(list(map(lambda t: t.term, post.tags))) if 'tags' in post else None, # 'tags':
                datetime.fromtimestamp(mktime(post.published_parsed)).strftime("%Y-%m-%d %H:%M:%S") # 'published_at':
            ]
            pgsql.run(SqlQueries.insert_into_staging_stackoverflow_jobs, parameters=registry)
        self.log.info("Done!")



