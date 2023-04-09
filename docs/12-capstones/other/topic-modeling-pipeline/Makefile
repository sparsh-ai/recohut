#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PROJECT_NAME = "big-data-ml"
REPO_NAME = "big-data-ml"
PYTHON_VERSION = "3.9.5"

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Run lint checks manually
lint:
	@echo "+ $@"
	@if [ ! -d .git ]; then git init && git add .; fi;
	@tox -e lint
.PHONY: lint

## Remove Python artifacts
clean-py:
	@echo "+ $@"
	@find ./src -type f -name "*.py[co]" -delete
	@find ./src -type d -name "__pycache__" -delete
.PHONY: clean-py

## Create AWS resources
aws-create:
	@echo "+ $@"
	@tox -e ci -- "create"
.PHONY: aws-create

## Create AWS SageMaker resources
aws-sagemaker-create:
	@echo "+ $@"
	@tox -e ci -- "sagemaker-create"
.PHONY: aws-sagemaker-create

## Provision EC2 instance, excluding Python pkg installation
provision-pre-python:
	@echo "+ $@"
	@tox -e provision -- "pre-python"
.PHONY: provision-pre-python

## Install Python packages on EC2 instance
provision-post-python:
	@echo "+ $@"
	@python3 src/ansible/playbook_utils.py --python-version 3
	@tox -e provision -- "post-python"
.PHONY: provision-post-python

## Stream Twitter data on EC2 instance
stream-start:
	@echo "+ $@"
	@tox -e stream -- --target-type="ec2"
.PHONY: stream-start

## Stop Stream of Twitter data on EC2 instance
stream-stop:
	@echo "+ $@"
	@tox -e stream -- --tag="stop" --target-type="ec2"
.PHONY: stream-stop

## Stream Twitter data locally, without saving to CSV or to S3 via Firehose
stream-local-start:
	@echo "+ $@"
	@tox -e stream
.PHONY: stream-local-start

## Stop Stream of Twitter data locally
stream-local-stop:
	@echo "+ $@"
	@tox -e stream -- --tag="stop"
.PHONY: stream-local-stop

## Directly run Stream of Twitter data locally
stream-check:
	@echo "+ $@"
	@tox -e stream_check
.PHONY: stream-check

## Delete AWS SageMaker resources
aws-sagemaker-delete:
	@echo "+ $@"
	@tox -e ci -- "sagemaker-delete"
.PHONY: aws-sagemaker-delete

## Destroy AWS resources
aws-destroy:
	@echo "+ $@"
	@tox -e ci -- "destroy"
	@python3 src/ansible/playbook_utils.py --python-version 2.7
.PHONY: aws-destroy

## Build dashboard
dash:
	@echo "+ $@"
	@tox -e dash
.PHONY: dash

## Run jupyterlab
build:
	@echo "+ $@"
	@tox -e build
.PHONY: build

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################



#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: help
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
