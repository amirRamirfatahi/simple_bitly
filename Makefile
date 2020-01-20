

install:
	pip install .


dev: 
	pip install -e .
	pip install -r requirements-dev.txt


test:
	pytest


.PHONY=install dev test

