"""
test_locations_etl_job.py
~~~~~~~~~~~~~~~

This module contains unit tests for the transformation steps of the ETL
job defined in locations_etl_job.py. It makes use of a local version of PySpark
that is bundled with the PySpark package.
"""
import unittest

from jobs.ETL.locations_etl_job import transform_data
import pyspark.sql.types as t
from tests.common import SparkETLTests
from tests.data import CleanedData


class LocationsETLTests(SparkETLTests):
    """Test suite for transformation in locations_etl_job.py"""

    def test_transform_data(self):
        """Test data transformer.

        Using small chunks of input data and expected output data, we
        test the transformation step to make sure it's working as
        expected.
        """

        intermediary_patent_df = self.spark.createDataFrame(
            data=CleanedData.intermediary_patent,
            schema=CleanedData.intermediary_patent_schema,
        )

        expected_data = [
            (
                "1af00b874ff3183021ca5c541e6f3e8d1bbb2b412bdb87f44cb07ae930dad646",
                "Albania",
                "EU",
            ),
        ]

        expected_data_schema = t.StructType(
            [
                t.StructField("location_id", t.StringType(), False),
                t.StructField("country", t.StringType(), False),
                t.StructField("continent", t.StringType(), False),
            ]
        )

        expected_data_df = self.spark.createDataFrame(
            data=expected_data, schema=expected_data_schema
        )

        data_transformed = transform_data(intermediary_patent_df)

        self.check_schema(data_transformed, expected_data_df)
        self.check_data(data_transformed, expected_data_df)


if __name__ == "__main__":
    unittest.main()
