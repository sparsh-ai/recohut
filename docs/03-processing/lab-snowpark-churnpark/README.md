# Lab: Churn Analytics Demo with dbt Snowpark Python models

PPT: https://docs.google.com/presentation/d/1IJSeE96bze7DECuDYqsTVv6FaOcNcJ5tTiCWKEku_QQ/edit#slide=id.g158d486fe9e_2_12

![](https://user-images.githubusercontent.com/62965911/214368208-6c5cdfa2-6f59-4b0a-9a69-8e9e30775c4d.svg)

## What is the Problem We Are Addressing?

- Over-the-top services or OTT is a category of media solutions that are in the form of apps that are distributed via mobile, tablet or TV (e.g., Netflix). The lines that traditionally separated players in the media segment are rapidly blurring. Streaming services (OTT most prominently), TV companies, and social networks are now competing over the same audiences. Radio stations, podcast companies, and streaming services are competing to provide radio and podcast content.
- As consumers get overwhelmed by the number of options, they will look to purge their subscriptions. Increased competition means media companies have to focus on content, user experience and loyalty, to create a more direct and lasting relationship with consumers.

## What Does this Demo Aim to Solve?

Based on customer subscription pattern, determine customer churn.

This demo is aimed at building dbt [python models](https://deploy-preview-1754--docs-getdbt-com.netlify.app/docs/building-a-dbt-project/building-models/python-models) with Snowflake.

## Architecture

![](https://user-images.githubusercontent.com/62965911/214368165-e9a96e9a-ee13-4d7a-825f-e8fc9fd66c97.svg)

## Files

[![Github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/sparsh-ai/recohut/tree/main/docs/03-processing/lab-snowpark-churnpark)

```
├── [1.9K]  README.md
├── [1.4K]  dbt_project.yml
├── [ 19K]  models
│   ├── [3.7K]  intermediate
│   │   └── [3.7K]  core
│   │       ├── [ 743]  _int_core__models.yml
│   │       ├── [ 656]  int_user_attributes.sql
│   │       └── [2.1K]  int_user_subscription_agg.py
│   ├── [3.8K]  marts
│   │   └── [3.7K]  predict
│   │       ├── [ 122]  predict_models.yml
│   │       └── [3.4K]  user_churn_predict_xgboost.py
│   ├── [8.6K]  ml
│   │   └── [8.5K]  features
│   │       ├── [ 420]  _int_features__models.yml
│   │       ├── [3.8K]  int_train_test.py
│   │       ├── [3.2K]  int_user_encoded.py
│   │       └── [ 907]  int_users_and_subscriptions.py
│   └── [2.8K]  staging
│       ├── [1.8K]  merkle
│       │   ├── [ 612]  _merkle__models.yml
│       │   ├── [ 216]  _merkle__sources.yml
│       │   └── [ 886]  stg_merkle__datasources.sql
│       └── [ 865]  ott
│           ├── [ 493]  _ott__models.yml
│           └── [ 244]  _ott__sources.yml
├── [  60]  packages.yml
└── [ 278]  setup
    └── [ 182]  setup.sql

  23K used in 11 directories, 18 files
```

## Notebooks

[![nbviewer](https://img.shields.io/badge/jupyter-notebook-informational?logo=jupyter)](https://nbviewer.org/github/sparsh-ai/recohut/blob/main/docs/03-processing/lab-snowpark-churnpark)