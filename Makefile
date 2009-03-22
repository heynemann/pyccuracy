# Makefile for Pyccuracy
#

# You can set these variables from the command line.


# Internal variables.


.PHONY: help build test upload docs selenium

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  build     to run a build"
	@echo "  test      to run all the tests"
	@echo "  upload    to run a build and upload to PyPI"
	@echo "  docs      to build documentation"
	@echo "  selenium  to fire selenium server"

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
    
test: build
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
	@python setup.py sdist upload
	@echo "Build finished and uploaded!"

docs:
	@$(MAKE) -C ./docs -f Makefile clean
	@$(MAKE) -C ./docs -f Makefile html
	tar -cf ./docs/current_docs.tar ./docs/build/html/*

selenium:
	@java -jar pyccuracy/lib/selenium-server/selenium-server.jar
