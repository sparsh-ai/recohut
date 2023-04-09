"""
test_dates_etl_job.py
~~~~~~~~~~~~~~~

This module contains unit tests for the transformation steps of the ETL
job defined in dates_etl_job.py. It makes use of a local version of PySpark
that is bundled with the PySpark package.
"""
import unittest

from datetime import datetime
from jobs.ETL.dates_etl_job import transform_data
import pyspark.sql.types as t
from tests.common import SparkETLTests
from tests.data import CleanedData


class DatesETLTests(SparkETLTests):
    """Test suite for transformation in dates_etl_job.py"""

    def test_transform_data(self):
        """Test data transformer.

        Using small chunks of input data and expected output data, we
        test the transformation step to make sure it's working as
        expected.
        """
        # assemble

        patent_cleaned_df = self.spark.createDataFrame(
            data=CleanedData.patent, schema=CleanedData.patent_schema
        )

        expected_data = [(datetime(2011, 1, 3), 2011), (datetime(2000, 9, 5), 2000)]
        expected_data_schema = t.StructType(
            [
                t.StructField("date", t.DateType(), False),
                t.StructField("year", t.IntegerType(), False),
            ]
        )

        expected_data_df = self.spark.createDataFrame(
            data=expected_data, schema=expected_data_schema
        )

        data_transformed = transform_data(patent_cleaned_df)

        self.check_schema(data_transformed, expected_data_df)
        self.check_data(data_transformed, expected_data_df)


if __name__ == "__main__":
    unittest.main()
