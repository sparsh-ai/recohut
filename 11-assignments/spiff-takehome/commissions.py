import json
import sqlite3
import pandas as pd
from dateutil.parser import parse

def create_database():
    """
    Helper function to create a sqlite3 database that will be used in the calculated_commission function.
    It will create two tables in the commission database: deals and products. 
    Args:
        None

    Returns:
        conn: A sqlite3 connection object that points to the commission database in the data directory
    """
    
    conn = sqlite3.connect('data/commissions.db')
    cursor = conn.cursor()
    
    #Create deals table
    cursor.execute('DROP TABLE IF EXISTS deals;')
    cursor.execute("""CREATE TABLE deals (
        id                      INTEGER PRIMARY KEY,
        sales_rep_name          TEXT,
        date                    TEXT,
        quantity_products_sold  INTEGER,
        product_id              INTEGER,
        has_2x_multiplier       INTEGER,
        FOREIGN KEY(product_id) REFERENCES products(id));""")
    
    #Create products table
    cursor.execute('DROP TABLE IF EXISTS products;')
    cursor.execute("""CREATE TABLE products (
        id              INTEGER PRIMARY KEY,
        name            TEXT,
        product_amount  INTEGER,
        commission_rate REAL );""")
       
    return conn  

    
def load_data(conn):
    """
    Helper function to populate the  database that will be used in the calculated_commission function.
    There are two tables in the commission database: deals and products.  The information for these tables
    is found in JSON files with their respective names in the data directory.

    Args:
        conn: A sqlite3 connection object that points to the commission database in the data directory

    Returns:
        conn: A sqlite3 connection object that points to the commission database in the data directory
    """
    tables = ['deals', 'products']
    cursor = conn.cursor()

    for table in tables:
        with open('data/{}.json'.format(table)) as f:
            data = json.load(f)

        columns = list(data[0].keys())
        query = "INSERT INTO {} VALUES (?{})".format(table, ",?"*(len(columns)-1))
        for item in data:
            values = tuple(item[c] for c in columns)
            cursor.execute(query, values)
    conn.commit()
    return conn


def calculate_commission(sales_rep_name, start_date, end_date):
    """
    Function/method to calculate commission for a sales rep in a given time period.

    Args:
        sales_rep_name (str): Name of the sales rep to calculate commission for.
        start_date (str): Starting date for the date range where commissions will be valid.
        end_date (str): Ending date for the date range where commissions will be valid.

    Returns:
        float: A single float value for total commission amount based on the input criteria. e.g. $749.48
    """
    
    conn = load_data(create_database())
    cursor = conn.cursor()
    start_date = parse(start_date).strftime('%Y-%m-%d')
    end_date = parse(end_date).strftime('%Y-%m-%d')
    query = """SELECT d.sales_rep_name, d.quantity_products_sold, d.has_2x_multiplier, p.product_amount, p.commission_rate
                FROM deals d 
                INNER JOIN products p
                ON d.product_id = p.id
                WHERE sales_rep_name = '{}'
                AND '{}' <= d.date 
                AND '{}' >= d.date""".format(sales_rep_name, start_date, end_date)
                
    df = pd.read_sql(query, con=conn)

    # Helper function to calculate commission from amounts in the dataframe columns
    def comm(row):
        commission = row['quantity_products_sold'] * row['product_amount'] * row['commission_rate']
#        if row['has_2x_multiplier'] == 1:
#            commission = commission * 2
        return round(commission,2)
    
    if df.empty:
        return 0.00
    else:
        df['commission'] = df.apply(lambda row: comm(row), axis=1)
        return df['commission'].sum()
