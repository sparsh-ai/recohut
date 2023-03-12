"""
test_details_etl_job.py
~~~~~~~~~~~~~~~

This module contains unit tests for the transformation steps of the ETL
job defined in details_etl_job.py. It makes use of a local version of PySpark
that is bundled with the PySpark package.
"""
import unittest

from jobs.ETL.details_etl_job import transform_data
import pyspark.sql.types as t
from tests.common import SparkETLTests
from tests.data import CleanedData


class DetailsETLTests(SparkETLTests):
    """Test suite for transformation in details_etl_job.py"""

    def test_transform_data(self):
        """Test data transformer.

        Using small chunks of input data and expected output data, we
        test the transformation step to make sure it's working as
        expected.
        """

        patent_cleaned_df = self.spark.createDataFrame(
            data=CleanedData.patent, schema=CleanedData.patent_schema
        )

        expected_data = [
            (
                "6114900",
                "A semiconductor memory device",
                "Semiconductor memory device ",
            ),
            (
                "D419739",
                "This process for the production of 2-keto-D",
                "Manufacturing independent constant current power",
            ),
            (
                "6018034",
                "A method of manufacturing a small",
                "Process for the production of 2-keto-D",
            ),
        ]

        expected_data_schema = t.StructType(
            [
                t.StructField("detail_id", t.StringType(), False),
                t.StructField("title", t.StringType(), False),
                t.StructField("abstract", t.StringType(), True),
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
