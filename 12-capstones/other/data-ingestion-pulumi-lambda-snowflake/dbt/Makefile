SHELL := /bin/bash
SOURCE_VENV := source ./venv/bin/activate


install:
	python3 -m venv venv \
		&& ${SOURCE_VENV} \
		&& python3 -m pip install --upgrade pip \
		&& pip install -r requirements.txt \
		&& dbt deps

dbt: dbt-run dbt-test dbt-docs

dbt-test:
	${SOURCE_VENV} && dbt test

dbt-run:
	${SOURCE_VENV} && dbt run

dbt-docs:
	${SOURCE_VENV} && dbt docs generate
