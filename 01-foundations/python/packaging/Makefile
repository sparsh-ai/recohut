install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt &&\
		pip install -r api/local/requirements.txt

.PHONY: src
src:
	jupyter nbconvert --output-dir='./src' --to script nbs/essentials/essentials.ipynb
	python ./src/essentials.py

.PHONY: api
api:
	black api/local/app/src/*.py

docs-serve:
	cd docs && npx docusaurus start

lint:
	pylint --disable=R,C src

test:
	python -m pytest -vv tests

all: install src