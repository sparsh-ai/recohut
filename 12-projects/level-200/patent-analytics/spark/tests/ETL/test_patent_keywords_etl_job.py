"""
test_patent_keywords_etl_job.py
~~~~~~~~~~~~~~~

This module contains unit tests for the transformation steps of the ETL
job defined in patent_keywords_etl_job.py. It makes use of a local version of PySpark
that is bundled with the PySpark package.
"""
import unittest

from jobs.ETL.patent_keywords_etl_job import transform_data
import pyspark.sql.types as t
from tests.common import SparkETLTests
from tests.data import KeywordExtractionData


class PatentKeywordsETLTests(SparkETLTests):
    """Test suite for transformation in patent_keywords_etl_job.py"""

    def test_transform_data(self):
        """Test data transformer.

        Using small chunks of input data and expected output data, we
        test the transformation step to make sure it's working as
        expected.
        """
        # assemble

        patent_keyword_df = self.spark.createDataFrame(
            data=KeywordExtractionData.patent_keyword, schema=KeywordExtractionData.patent_keyword_schema
        )

        expected_data = [
            (
                "5a5080d0ba16d86a9950465d5d7f08a36b095de84c3fc79f81e552e43b580eae",
                "6114900",
                "test",
            ),
            (
                "9b996471fd62b5bf3c648adc20002b60156ed0b75ca49c837df433fbddfebbc2",
                "6114900",
                "test2",
            ),
            (
                "e871d4dc6113889350547b6a1abd759a06a01437f8f790763dce5501ce7209be",
                "6114900",
                "test3",
            ),
            (
                "80752e75e35589aa27187818a9178965ac749ecc2c9c03218d11b68f59fbaa83",
                "D419739",
                "semiconductor",
            ),
            (
                "4027efe3eb72dcede20b09785be98af7debb5d1ee174208e022204effcc463cd",
                "D419739",
                "pool",
            ),
            (
                "148557910606d577f0c2fbcd9383a95f5d677d272ec240e1a82270d5e7580759",
                "6018034",
                "mechanic",
            ),
        ]
        expected_data_schema = t.StructType(
            [
                t.StructField("patent_keyword_id", t.StringType(), False),
                t.StructField("patent_id", t.StringType(), False),
                t.StructField("keyword", t.StringType(), False),
            ]
        )

        expected_data_df = self.spark.createDataFrame(
            data=expected_data, schema=expected_data_schema
        )

        data_transformed = transform_data(patent_keyword_df)

        self.check_schema(data_transformed, expected_data_df)
        self.check_data(data_transformed, expected_data_df)


if __name__ == "__main__":
    unittest.main()
