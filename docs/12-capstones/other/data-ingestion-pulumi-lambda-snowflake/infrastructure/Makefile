SHELL := /bin/bash
SOURCE_VENV := source ./venv/bin/activate

install:
	python3 -m venv venv && \
		${SOURCE_VENV} && \
		python3 -m pip install --upgrade pip \
		pip install -r requirements.txt

up:
	${SOURCE_VENV} && pulumi up
