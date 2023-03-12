#!/usr/bin/env bash
./build_dependencies.sh
cp -r jobs ../airflow/dags/scripts
cp -r configs ../airflow/dags/scripts
cp packages.zip ../airflow/dags/scripts/dependencies/