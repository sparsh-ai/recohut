"""
test_intermediary_etl_job.py
~~~~~~~~~~~~~~~

This module contains unit tests for the transformation steps of the ETL
job defined in intermediary_patent_etl_job.py. It makes use of a local version of PySpark
that is bundled with the PySpark package.
"""
import unittest

from jobs.ETL.intermediary_patent_etl_job import transform_data
from tests.common import SparkETLTests
from tests.data import CleanedData


class IntermediaryPatentETLTests(SparkETLTests):
    """Test suite for transformation in intermediary_patent_etl_job.py"""

    def test_transform_data(self):
        """Test data transformer.

        Using small chunks of input data and expected output data, we
        test the transformation step to make sure it's working as
        expected.
        """
        # assemble

        patent_df = self.spark.createDataFrame(
            data=CleanedData.patent, schema=CleanedData.patent_schema
        )

        patent_assignee_df = self.spark.createDataFrame(
            data=CleanedData.patent_assignee, schema=CleanedData.patent_assignee_schema
        )

        assignee_df = self.spark.createDataFrame(
            data=CleanedData.assignee, schema=CleanedData.assignee_schema
        )

        patent_inventor_df = self.spark.createDataFrame(
            data=CleanedData.patent_inventor, schema=CleanedData.patent_inventor_schema
        )

        inventor_df = self.spark.createDataFrame(
            data=CleanedData.inventor, schema=CleanedData.inventor_schema
        )

        location_df = self.spark.createDataFrame(
            data=CleanedData.location, schema=CleanedData.location_schema
        )

        expected_data_df = self.spark.createDataFrame(
            data=CleanedData.intermediary_patent,
            schema=CleanedData.intermediary_patent_schema,
        )

        data_transformed = transform_data(
            patent=patent_df,
            patent_assignee=patent_assignee_df,
            assignee=assignee_df,
            patent_inventor=patent_inventor_df,
            inventor=inventor_df,
            location=location_df,
        )

        self.check_schema(data_transformed, expected_data_df)
        self.check_data(data_transformed, expected_data_df)


if __name__ == "__main__":
    unittest.main()
