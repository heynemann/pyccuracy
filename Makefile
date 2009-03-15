# Makefile for Pyccuracy
#

# You can set these variables from the command line.


# Internal variables.


.PHONY: help build tests upload

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  build     to run a build"
	@echo "  tests     to run all the tests"
	@echo "  upload    to run a build and upload to PyPI"

build:
	@echo "=================="
	@echo "Starting the build"
	@echo "=================="
	@rm -f -r ./pyccuracy/build
	@rm -f -r ./pyccuracy/*.pyc
	@rm -f -r ./pyccuracy/actions/*.pyc
	@python -m compileall ./pyccuracy
	@echo "==============="
	@echo "Build finished!"
	@echo "==============="
    
tests: build
	@echo "================="
	@echo "Starting tests..."
	@echo "================="
	
	@for f in `ls tests | grep --regex="test_.*\.py$$"` ; do \
		cd tests && python $$f && cd .. && echo $$env; \
	done
	
	@python ./tests/action_tests/test_all.py
	
upload:
	@echo "Running a build..."
	@echo off
	@rm -f -r ./pyccuracy/build
	@setup.py sdist upload
	@echo "Build finished and uploaded!"
	
