"""
test_owners_etl_job.py
~~~~~~~~~~~~~~~

This module contains unit tests for the transformation steps of the ETL
job defined in owners_etl_job.py. It makes use of a local version of PySpark
that is bundled with the PySpark package.
"""
import unittest

from jobs.ETL.owners_etl_job import transform_data
import pyspark.sql.types as t
from tests.common import SparkETLTests
from tests.data import CleanedData


class OwnersETLTests(SparkETLTests):
    """Test suite for transformation in owners_etl_job.py"""

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
                "23d67e983020b217078bba89b0b8de9f00e41f742669dad1090bde4044bf9dd6",
                "company",
                "Rainbow Display, Inc.",
            ),
            (
                "73b561e3245e37e271ada78c73f5b2112b2394393ed3ae39e1e7ee311db87657",
                "individual",
                "A. Chacko George",
            ),
        ]

        expected_data_schema = t.StructType(
            [
                t.StructField("owner_id", t.StringType(), False),
                t.StructField("type", t.StringType(), False),
                t.StructField("name", t.StringType(), False),
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
