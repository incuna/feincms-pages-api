SHELL := /bin/bash

help:
	@echo "Usage:"
	@echo " make help    -- displays this help"
	@echo " make test    -- runs tests"
	@echo " make release -- releases the library to internal pypi"

test:
	./pages/tests/run.py

release:
	python setup.py register sdist bdist_wheel upload
