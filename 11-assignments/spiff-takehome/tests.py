import commissions as c
import pytest
import sqlite3

#Test for commissions that do not fall within starting and ending dates
def test1():
    commission = c.calculate_commission(sales_rep_name="Ian", start_date="2022-01-01", end_date="2022-5-30")
    assert commission == 0.00

#Test for commission when sales_rep_name is not in database
def test2():
    commission = c.calculate_commission(sales_rep_name="Jan", start_date="2023-01-01", end_date="2023-5-30")
    assert commission == 0.00

#Test date when starting and ending date are the same
def test3():
    commission = c.calculate_commission(sales_rep_name="Ian", start_date="2023-01-15", end_date="2023-01-15")
    assert commission == 22030.00

#Test for date input when month doesn't have a trailing 0
def test4():
    commission = c.calculate_commission(sales_rep_name="Ian", start_date="2023-01-01", end_date="2023-4-30")
    assert commission == 55350.00

#Test for date input when day doesn't have a trailing 0
def test4():
    commission = c.calculate_commission(sales_rep_name="Ian", start_date="2023-01-1", end_date="2023-04-30")
    assert commission == 55350.00

#Test for accuracy
def test5():
    commission = c.calculate_commission(sales_rep_name="David", start_date="2023-04-01", end_date="2023-06-30")
    assert commission == 89540.00

#Test for accuracy
def test6():
    commission = c.calculate_commission(sales_rep_name="Poppy", start_date="2023-03-01", end_date="2023-5-30")
    assert commission == 118190.00



