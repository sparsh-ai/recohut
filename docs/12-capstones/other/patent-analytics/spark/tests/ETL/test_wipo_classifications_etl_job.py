"""
test_wipo_classifications_etl_job.py
~~~~~~~~~~~~~~~

This module contains unit tests for the transformation steps of the ETL
job defined in wipo_classifications_etl_job.py. It makes use of a local version of PySpark
that is bundled with the PySpark package.
"""
import unittest

from jobs.ETL.wipo_classifications_etl_job import transform_data
import pyspark.sql.types as t
from tests.common import SparkETLTests
from tests.data import CleanedData


class WipoClassificationsETLTests(SparkETLTests):
    """Test suite for transformation in wipo_classifications_etl_job.py"""

    def test_transform_data(self):
        """Test data transformer.

        Using small chunks of input data and expected output data, we
        test the transformation step to make sure it's working as
        expected.
        """

        wipo_df = self.spark.createDataFrame(
            data=CleanedData.wipo, schema=CleanedData.wipo_schema
        )

        wipo_field_df = self.spark.createDataFrame(
            data=CleanedData.wipo_field, schema=CleanedData.wipo_field_schema
        )

        expected_data = [
            ("6114900", "Electrical engineering", "Electrical machinery, apparatus"),
            ("D419739", "Instruments", "Measurement"),
            ("6018034", "Instruments", "Control"),
        ]

        expected_data_schema = t.StructType(
            [
                t.StructField("wipo_classification_id", t.StringType(), False),
                t.StructField("sector", t.StringType(), False),
                t.StructField("field", t.StringType(), False),
            ]
        )

        expected_data_df = self.spark.createDataFrame(
            data=expected_data, schema=expected_data_schema
        )

        data_transformed = transform_data(
            wipo_data=wipo_df, wipo_field_data=wipo_field_df
        )

        self.check_schema(data_transformed, expected_data_df)
        self.check_data(data_transformed, expected_data_df)


if __name__ == "__main__":
    unittest.main()
