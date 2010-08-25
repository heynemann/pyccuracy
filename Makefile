# Makefile for Pyccuracy
SHELL := /bin/bash

# Internal variables.
root_dir=.
build_dir=${root_dir}/build
src_dir=${root_dir}/pyccuracy

tests_dir=${root_dir}/tests
unit_tests_dir=${tests_dir}/unit
functional_tests_dir=${tests_dir}/functional

compile_log_file=${build_dir}/compile.log
unit_log_file=${build_dir}/unit.log
functional_log_file=${build_dir}/functional.log

browser="firefox"
pattern="*"

help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  all         to run a complete build"
	@echo "  clean       to clear the build dir"
	@echo "  compile     to compile all python files"
	@echo "  test        to run all the tests"
	@echo "  unit        to run all the unit tests"
	@echo "  functional  to run all the functional tests"
	@echo "  acceptance  to run all the acceptance tests"
	@echo "  docs        to build documentation"

all: prepare_build compile test report_success
test: prepare_build compile run_unit run_functional acceptance report_success
unit: prepare_build compile run_unit report_success
functional: prepare_build compile run_functional report_success
prepare_build: clean create_build_dir
clean: remove_build_dir remove_dist_dir
	@find . -name '*.pyc' -delete

# action targets

report_success:
	@echo "Build succeeded!"

remove_build_dir:
	@rm -fr ${build_dir}

remove_dist_dir:
	@rm -fr dist/
	@rm -fr Pyccuracy.egg-info/

create_build_dir:
	@mkdir -p ${build_dir}

compile:
	@echo "Compiling source code..."
	@rm -f ${compile_log_file} >> /dev/null
	@rm -f -r ${src_dir}/*.pyc >> /dev/null
	@python -tt -m compileall ${src_dir} >> ${compile_log_file} 2>> ${compile_log_file}
	@python -tt -m compileall ${unit_tests_dir} >> ${compile_log_file} 2>> ${compile_log_file}

run_all_tests: compile
	@echo "Running all tests..."
	@nosetests -s --verbose --with-coverage --cover-package=pyccuracy

run_unit: compile
	@echo "Running unit tests..."
	@rm -f ${unit_log_file} >> /dev/null
	@nosetests -s --verbose --with-coverage --cover-package=pyccuracy ${unit_tests_dir}

run_functional: compile
	@echo "Running functional tests..."
	@rm -f ${functional_log_file} >> /dev/null
	@nosetests -s --verbose --with-coverage --cover-package=pyccuracy ${functional_tests_dir}

selenium_up:
	@echo "===================="
	@echo "Starting selenium..."
	@echo "===================="
	@java -jar ${root_dir}/lib/selenium-server.jar 2> /dev/null > /dev/null &
	@echo "Started."

selenium_down:
	@echo "==================="
	@echo "Killing selenium..."
	@echo "==================="
	@-ps aux | egrep selenium | egrep -v egrep | awk '{ print $$2 }' | xargs kill -9
	@echo "Killed."

wait:
	@echo "=========="
	@echo "Waiting..."
	@echo "=========="
	@sleep 10

acceptance:
	@make selenium_up
	@make wait
	@echo "================="
	@echo "Starting tests..."
	@echo "================="

	@PYTHONPATH=`pwd`/pyccuracy/:$$PYTHONPATH python pyccuracy/pyccuracy_console.py -d ${root_dir}/tests/acceptance/action_tests/ -p "${pattern}en-us.acc" -l en-us -v 3 -b ${browser}
	@PYTHONPATH=`pwd`/pyccuracy/:$$PYTHONPATH python pyccuracy/pyccuracy_console.py -d ${root_dir}/tests/acceptance/action_tests/ -p "${pattern}pt-br.acc" -l pt-br -v 3 -b ${browser}
	@-make selenium_down

dist: clean
	@echo "Running a build..."
	@python setup.py sdist
	@echo "Build finished successfully!"

upload: clean
	@echo "Running a build..."
	@python setup.py sdist upload
	@echo "Build finished successfully and uploaded!"

docs:
	@python pyccuracy/actions/core/__init__.py > actions_reference.textile
	@echo -e "\nFile 'actions_reference.textile' was generated.\n"
	@echo -e "Don't forget to update http://pyccuracy.org/actions-reference.\n"

deb:
	mv .git /tmp/pyccuracy_git
	python -c 'import os;os.system("debuild -tc")'
	mv /tmp/pyccuracy_git .git
	mv ../python-pyccuracy_*.deb ./releases
