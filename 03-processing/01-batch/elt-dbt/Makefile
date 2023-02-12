init:
	dbt init ${PROJECT_NAME}
debug:
	dbt debug
run:
# If you are in dbt directory already, you don't need to export the `DBT_PROFILES_DIR` environment variable otherwise you can export it to run dbt from other folders also
	export DBT_PROFILES_DIR=path/to/directory
	dbt run
# Alternative way is to directly mention the profile path while running the dbt project
	dbt run --profiles-dir path/to/directory
test:
# Running dbt test without mentioning any models will test all the models in the dbt project
	dbt test
# If you want to test only specific models, you can use this format
	dbt test -m model1 [model2]
seed:
	dbt seed
venv:
	pipenv --python 3.9.7
	pipenv install
	pipenv shell
	pipenv --venv
	pipenv --rm