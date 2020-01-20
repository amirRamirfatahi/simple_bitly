

install:
	pip install .


dev: 
	pip install -e .
	pip install -r requirements-dev.txt


test:
	pytest


ci:
	pip install -e .
	pip install -r requirements-ci.txt


cover:
	pytest tests --cov=simplebitly


.PHONY=install dev test ci

