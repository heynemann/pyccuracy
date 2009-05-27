# Makefile for Pynq
SHELL := /bin/bash

# Internal variables.
file_version=0.5.1
root_dir=.
build_dir=${root_dir}/build
src_dir=${root_dir}/pyccuracy

tests_dir=${root_dir}/tests
unit_tests_dir=${tests_dir}/unit

compile_log_file=${build_dir}/compile.log
unit_log_file=${build_dir}/unit.log

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  build     to run a build"
	@echo "  test      to run all the tests"
	@echo "  unit      to run all the unit tests"
	@echo "  upload    to run a build and upload to PyPI"
	@echo "  docs      to build documentation"

all: prepare_build compile test report_success
unit: prepare_build compile run_unit report_success
prepare_build: clean create_build_dir
clean: remove_build_dir remove_dist_dir

# action targets

report_success:
	@echo "Build succeeded!"

remove_build_dir:
	@rm -fr ${build_dir}

remove_dist_dir:
	@rm -fr dist/
	@rm -fr Pynq.egg-info/

create_build_dir:
	@mkdir -p ${build_dir}

compile:
	@echo "Compiling source code..."
	@rm -f ${compile_log_file} >> /dev/null
	@rm -f -r ${src_dir}/*.pyc >> /dev/null
	@python -m compileall ${src_dir} >> ${compile_log_file} 2>> ${compile_log_file}

run_unit: compile
	@echo "Running unit tests..."
	@rm -f ${unit_log_file} >> /dev/null
	@if [ "$(nocoverage)" = "true" ]; then nosetests --verbose ${unit_tests_dir}; else nosetests --verbose --with-coverage --cover-package=pyccuracy; fi
	@echo "============="
	@echo "Unit coverage"
	@echo "============="
	@if [ "$(nocoverage)" != "true" ]; then cat ${unit_log_file} | egrep '(Name)|(TOTAL)'; fi
	@if [ "$(nocoverage)" = "true" ]; then echo 'Coverage Disabled.'; fi
	@echo

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

deb:
	mv .git /tmp/pyccuracy_git
	python -c 'import os;os.system("debuild")'
	mv /tmp/pyccuracy_git .git
