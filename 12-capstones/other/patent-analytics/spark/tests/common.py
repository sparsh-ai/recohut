import unittest

from dependencies.spark import start_spark
import pyspark.sql.dataframe as dataframe


class SparkETLTests(unittest.TestCase):
    def setUp(self):
        """Start Spark"""
        self.spark, *_ = start_spark()
        self.test_data_path = "test_data/"

    def tearDown(self):
        """Stop Spark"""
        self.spark.stop()

    # test_schema method is originating from https://towardsdatascience.com/testing-pyspark-dataframe-transformations-d3d16c798a84
    @staticmethod
    def check_schema(
        df1: dataframe.DataFrame, df2: dataframe.DataFrame, check_nullable=False
    ):
        field_list = lambda field: (field.name, field.dataType, field.nullable)
        fields1 = [*map(field_list, df1.schema.fields)]
        fields2 = [*map(field_list, df2.schema.fields)]
        if check_nullable:
            res = set(fields1) == set(fields2)
        else:
            res = set([field[:-1] for field in fields1]) == set(
                [field[:-1] for field in fields2]
            )
        return res

    # test_data method is originating from https://towardsdatascience.com/testing-pyspark-dataframe-transformations-d3d16c798a84
    @staticmethod
    def check_data(df1: dataframe.DataFrame, df2: dataframe.DataFrame):
        data1 = df1.collect()
        data2 = df2.collect()
        return set(data1) == set(data2)


if __name__ == "__main__":
    unittest.main()
