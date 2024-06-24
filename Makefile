# https://raw.githubusercontent.com/awslabs/serverless-application-model/master/Makefile

.PHONY: test deploy clean all sdist

all: clean test sdist

target:
	$(info ${HELP_MESSAGE})
	@exit 0

dev:
	pip install -e '.[all]'

black:
	black alphahunt_sdk

test:
	ALPHAHUNT_TOKEN="" pytest -sv

dist: sdist

sdist: clean
	python -m build

clean:
	rm -rf `find . | grep \.pyc`
	rm -f dist/*

publish:
	twine upload -r h dist/alphahunt-sdk-*.tar.gz

define HELP_MESSAGE

Usage: $ make [TARGETS]

TARGETS
	all	    Build the deploy.zip ONLY
	test        Run the tests
	deploy      Build the deploy.zip for uloading to Lambda
	clean       Cleanup .pyc and deploy files

endef
