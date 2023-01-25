install:
	pip install -r requirements.txt

version:
	prefect version

start:
	prefect orion start

cloud:
	prefect cloud login --key ${KEY} --workspace "sparshcloudgmailcom/sparshcloud"

storage:
	prefect storage create

open-api-docs:
	open http://127.0.0.1:4200/docs
	open http://127.0.0.1:4200/redoc

open-ui:
	open http://localhost:4200

set-api:
	prefect config set PREFECT_API_URL=http://127.0.0.1:4200/api

deploy:
	prefect deployment create ${your_file}.py

work-queue:
	prefect work-queue create --tag tutorial tutorial_queue

work-queue-ls:
	prefect work-queue ls

agent-start:
	prefect agent start '<work-queue-id>'