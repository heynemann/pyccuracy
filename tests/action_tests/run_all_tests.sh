#!/bin/sh
echo Running All Tests

for file in `ls test_*.py`; do `./run_test.sh $file`; done