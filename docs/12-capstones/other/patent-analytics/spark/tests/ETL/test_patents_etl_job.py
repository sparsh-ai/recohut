"""
test_patents_etl_job.py
~~~~~~~~~~~~~~~

This module contains unit tests for the transformation steps of the ETL
job defined in patents_etl_job.py. It makes use of a local version of PySpark
that is bundled with the PySpark package.
"""
import unittest

from datetime import datetime
from jobs.ETL.patents_etl_job import transform_data
import pyspark.sql.types as t
from tests.common import SparkETLTests
from tests.data import CleanedData


class PatentsETLTests(SparkETLTests):
    """Test suite for transformation in patents_etl_job.py"""

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
        patent_df = self.spark.createDataFrame(
            data=CleanedData.patent, schema=CleanedData.patent_schema
        )

        expected_data = [
            (
                "6114900",
                datetime(2000, 9, 5),
                "6114900",
                "23d67e983020b217078bba89b0b8de9f00e41f742669dad1090bde4044bf9dd6",
                None,
                "6114900",
                2,
            ),
            (
                "D419739",
                datetime(2011, 1, 3),
                "D419739",
                "73b561e3245e37e271ada78c73f5b2112b2394393ed3ae39e1e7ee311db87657",
                "1af00b874ff3183021ca5c541e6f3e8d1bbb2b412bdb87f44cb07ae930dad646",
                "D419739",
                3,
            ),
            ("6018034", datetime(2011, 1, 3), "6018034", None, None, "6018034", 4),
        ]

        expected_data_schema = t.StructType(
            [
                t.StructField("id", t.StringType(), False),
                t.StructField("granted_date", t.DateType(), False),
                t.StructField("detail_id", t.StringType(), False),
                t.StructField("owner_id", t.StringType(), True),
                t.StructField("location_id", t.StringType(), True),
                t.StructField("wipo_classification_id", t.StringType(), False),
                t.StructField("num_claims", t.IntegerType(), False),
            ]
        )

        expected_data_df = self.spark.createDataFrame(
            data=expected_data, schema=expected_data_schema
        )

        data_transformed = transform_data(
            patent=patent_df, intermediary_patent=intermediary_patent_df
        )

        self.check_schema(data_transformed, expected_data_df)
        self.check_data(data_transformed, expected_data_df)


if __name__ == "__main__":
    unittest.main()
