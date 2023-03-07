# Inegi Snowflake Datamodel

> National Institute of Statistics and Geography

In this workshop, we will:

1. Download the data
2. Preprocess and Transform
3. Load into Snowflake
4. Data Modeling with Snowpark

## Snowflake Objects

![](https://user-images.githubusercontent.com/62965911/211294409-8070a0d0-21ba-4861-8ca2-4da4090b37a8.png)

## Solution

```
.
├── [ 27K]  01-sa-lab-1-inegi-snowpark.ipynb
├── [272M]  data
│   └── [272M]  inegi
│       ├── [166M]  csv
│       │   ├── [ 23M]  inegi.csv
│       │   └── [143M]  iter_00_cpv2020
│       │       ├── [ 528]  catalogos
│       │       │   └── [ 432]  tam_loc.csv.csv
│       │       ├── [143M]  conjunto_de_datos
│       │       │   └── [143M]  conjunto_de_datos_iter_00CSV20.csv
│       │       ├── [ 70K]  diccionario_datos
│       │       │   └── [ 70K]  diccionario_datos_iter_00CSV20.csv
│       │       └── [2.1K]  metadatos
│       │           └── [2.1K]  metadatos_iter_00_cpv2020.txt
│       ├── [ 35M]  iter_00_cpv2020_csv.zip
│       └── [ 72M]  json
│           ├── [9.1M]  inegi1.json
│           ├── [979K]  inegi1.json.gz
│           ├── [9.1M]  inegi2.json
│           ├── [991K]  inegi2.json.gz
│           ├── [9.3M]  inegi3.json
│           ├── [1.1M]  inegi3.json.gz
│           ├── [9.2M]  inegi4.json
│           ├── [1.1M]  inegi4.json.gz
│           ├── [9.3M]  inegi5.json
│           ├── [1.2M]  inegi5.json.gz
│           ├── [9.1M]  inegi6.json
│           ├── [1.0M]  inegi6.json.gz
│           ├── [9.1M]  inegi7.json
│           ├── [1.1M]  inegi7.json.gz
│           ├── [1.8K]  inegi8.json
│           └── [ 501]  inegi8.json.gz
├── [ 358]  inegi.mdx
└── [1.4K]  src
    └── [1.3K]  entidad.py

 272M used in 10 directories, 25 files
```