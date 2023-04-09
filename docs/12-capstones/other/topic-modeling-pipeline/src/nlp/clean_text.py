#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""Process text with PySpark."""


from pyspark.sql import Column
from pyspark.sql import functions as F


def remove_punctuation(column_obj: Column) -> Column:
    """Removes punctuation from a DataFrame text column."""
    return F.regexp_replace(column_obj, "\\p{Punct}", "")


def remove_lead_trail_spaces(column_obj: Column) -> Column:
    """Removes leading and trailing spaces from a DataFrame text column."""
    return F.trim(column_obj)


def replace_multiple_spaces(column_obj: Column) -> Column:
    """Replace multiple spaces with a single space."""
    return F.regexp_replace(column_obj, r"\s+", " ")
