# Lab: Postgres e-Wallet Data Model

In this lab, we will design a data model for an eWallet company.

One of the online retail company’s features is an e-wallet service, that holds credit that can be used to pay for products purchased on the platform.

Users can receive credit in three different ways:

1. When a product purchase that is paid for is canceled, the money is refunded as cancellation credit.
2. Users can receive gift card credit as a gift.
3. If a user has a poor service experience, soo-sorry credit may be provided.

Credit in the e-wallet expires after 6 months if it is gift card credit and soo-sorry credit, but in 1 year if it is cancellation credit.

The Finance department of the company would like to build reporting and analytics on the e-wallet service so they can understand the extent of the wallet liabilities the company has.

Some of the questions they would want to answer from this are like below:

1. What is the daily balance of credit in the e-wallet service?
2. How much credit will expire in the next month?
3. What is the outcome (i.e. % used, % expired, % left) of credit given in a particular month?

## Background

One of the online retail company’s features is an e-wallet service, that holds credit that can be used to pay for products purchased on the platform.

Users can receive credit in three different ways:

1. When a product purchase that is paid for is canceled, the money is refunded as cancellation credit.
2. Users can receive gift card credit as a gift.
3. If a user has a poor service experience, soo-sorry credit may be provided.

Credit in the e-wallet expires after 6 months if it is gift card credit and soo-sorry credit, but in 1 year if it is cancellation credit.

## Requirement

The Finance department of the company would like to build reporting and analytics on the e-wallet service so they can understand the extent of the wallet liabilities the company has.

Some of the questions they would want to answer from this are like below:

1. What is the daily balance of credit in the e-wallet service?
2. How much credit will expire in the next month?
3. What is the outcome (i.e. % used, % expired, % left) of credit given in a particular month?

### Solution Design

The four key decisions made during the design of a dimensional model include:

1. Select the business process. 2. Declare the grain. 3. Identify the dimensions. 4. Identify the facts.

Let’s write down this decision steps for our e-Wallet case:

1. Assumptions: Design is developed based on the background (Business Process) given but also keeping flexibility in mind. All the required fields are assumed to be available from the company’s transactional database.

2. Grain definition: Atomic grain refers to the lowest level at which data is captured by a given business process.

The lowest level of data that can be captured in this context is wallet transactions i.e., all the credit and debit transactions on e-wallet.

3. Dimensions: Dimensions provide the “who, what, where, when, why, and how” context surrounding a business process event.

### Dimension Tables

DimWallet:

| Columns | Comment       |
| ------- | ------------- |
| Wallet\_Id    | Unique identifier for wallet credit |
| Type          | Wallet credit type ('giftcard','cancellation','goodwill') |
| Start\_Date   | Wallet credit start date |
| Expiry\_Date  | Wallet credit expiry date |
| Wallet\_price | Price of wallet credit |

DimCustomer:

| Columns | Comment           |
| ------- | ----------------- |
| Customer\_ID      | Surrogate key used to uniquely identify Customer details |
| dim\_Customer\_ID | Unique identifier for customer |
| First\_Name       | First name of the customer |
| Last\_Name        | Second name of the customer |
| Gender            | Gender of the customer |
| Birth\_Date       | Date of birth of customer |
| Email             | Email address of the customer |
| Address           | Resident address of the customer |
| Start\_Date       | To handle Slowly Changing Dimension of customer details of Customers like address etc |
| End\_Date         | To handle SCD |

FactWallet:

| Columns | Comment           |
| ------- | ----------------- |
| Transaction\_Id   | Standalone primary key for fact |
| Customer\_ID      | Foreign key to DimCustomer |
| Transaction\_Date | Date of transaction and foriengn key to DimDate |
| Wallet\_Id        | Foreign key to DimWallet |
| Type              | Type of transaction (Credit, Debit) |
| Credit            | Credit amount |
| Debit             | Debit amount |

## STAR schema model

Below is the logical diagram of the dimensional model for the eWallet service:

![](https://user-images.githubusercontent.com/62965911/211739605-e344b5cb-9b62-445c-bbc1-386d9d2c6718.png)

## Assignment

1. Load the Tables into Database
2. Create views to answer the 3 questions asked by the finance department team
3. Create PR for your solution and add Instructor and a peer for review

## Files

[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sparsh-ai/recohut/tree/main/docs/04-data-modeling/lab-postgres-ewallet-datamodel)

```
├── [ 25K]  01-sa-generate-synthetic-data.ipynb
├── [5.3K]  README.md
└── [8.5K]  data
    ├── [1.5K]  customer.csv
    ├── [6.5K]  transactions.csv
    └── [ 437]  wallet.csv

  39K used in 1 directory, 5 files
```

## Notebooks

[![nbviewer](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/recohut/blob/main/docs/04-data-modeling/lab-postgres-ewallet-datamodel)