# Spiff Data Engineering Candidate Coding Exercises

This is the repo for the data engineering exercise that is part of the interview process for a data engineering role at Spiff.  

### Solution

The function/method that was created for this project is:

```py
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

    return total_commission
```

### Dependencies

A list of the packages required to run this method are listed in the requirements.txt file.  To install the requirements type the following on the command line:

```sh
pip install -r requirements.txt
```

### Data

The input data can be found in the "data" folder of this repo. It contains two tables worth of data in .json format (one for the Deals and one for the Products). The Deals data contains information about an individual deal that was sold (i.e. sales_rep_name, date, quantity_products_sold, product_id) and the Products data contains related data about the products such as product_amount and the commission rate for that product. In order to get all of the data needed to calculate the commission the Deals data will require additional information from the Product table (product_id form Deals is the reference id of the Products data).

### How to Run

This method is contained in the commission.py file.  To run this method, import the commission.py module into your python program and then use the following function call:

```py
calculate_commission(sales_rep_name, start_date, end_date):
```

Alternatively, you can run this method on the command line in the same directory as the commissions.py file with the following prompts:

```sh
python 
>>> import commissions as c
>>> c.calculate_commission("Ian", "2023-01-15", "2023-04-30")
```

### Tests

Several unit tests have been included in this repo.  To run these tests type the following on the command line:

```sh
pytest tests.py
```



