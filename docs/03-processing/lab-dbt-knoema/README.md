# Lab: dbt Snowflake on Knoema data

In this lab, we are going to analyze historical trading performance of a company that has trading desks spread across different regions. As inputs, we are going to leverage datasets available in Knoema Economy Data Atlas that is available in Snowflake Data Marketplace, plus few manual uploads.

We are going to set up the environments from scratch, build scalable pipelines in dbt, establish data tests, and Snowflake and promote code to production. Finally we will use Snowsight to build a simple dashboard to visualize the results.

![](https://user-images.githubusercontent.com/62965911/214300316-806a0124-09ba-4286-a6dd-8e908a72046c.png)

![](https://user-images.githubusercontent.com/62965911/214300221-3c3c2698-a03e-4e2e-a5fb-757e079a7f46.png)

![](https://user-images.githubusercontent.com/62965911/214300288-d5429151-4ce0-4509-ba4c-97a891893c6b.png)

## Files

[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sparsh-ai/recohut/tree/main/docs/03-processing/lab-dbt-knoema)

```
├── [1.3K]  README.md
├── [ 684]  dbt_project.yml
├── [ 844]  macros
│   └── [ 748]  call_me_anything_you_want.sql
├── [ 16K]  main.ipynb
├── [8.4K]  models
│   ├── [1.2K]  example
│   │   ├── [ 475]  my_first_dbt_model.sql
│   │   ├── [ 115]  my_second_dbt_model.sql
│   │   └── [ 437]  schema.yml
│   ├── [1.3K]  l10_staging
│   │   ├── [ 285]  base_knoema_fx_rates.sql
│   │   ├── [ 668]  base_knoema_stock_history.sql
│   │   └── [ 169]  sources.yml
│   ├── [4.4K]  l20_transform
│   │   ├── [  91]  tfm_book.sql
│   │   ├── [ 450]  tfm_daily_position.sql
│   │   ├── [ 769]  tfm_daily_position_with_trades.sql
│   │   ├── [ 235]  tfm_fx_rates.sql
│   │   ├── [ 483]  tfm_knoema_stock_history.sql
│   │   ├── [ 395]  tfm_knoema_stock_history_alt.sql
│   │   ├── [  59]  tfm_stock_history.sql
│   │   ├── [ 750]  tfm_stock_history_major_currency.sql
│   │   └── [ 874]  tfm_trading_pnl.sql
│   ├── [ 844]  l30_mart
│   │   ├── [ 358]  fct_trading_pnl.sql
│   │   ├── [  98]  fct_trading_pnl_finance_view.sql
│   │   ├── [  98]  fct_trading_pnl_risk_view.sql
│   │   └── [  98]  fct_trading_pnl_treasury_view.sql
│   └── [ 588]  tests
│       └── [ 492]  data_quality_tests.yml
├── [  61]  packages.yml
├── [ 449]  profiles.yml
└── [1.0K]  seeds
    ├── [ 532]  manual_book1.csv
    └── [ 394]  manual_book2.csv

  29K used in 8 directories, 28 files
```

## Notebooks

[![nbviewer](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/recohut/blob/main/docs/03-processing/lab-dbt-knoema)