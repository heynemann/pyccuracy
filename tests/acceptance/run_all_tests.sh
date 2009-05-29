#!/bin/bash
for i in $( ls | grep --regex="test_.*\.py$" ); do
    echo =================================================
    echo    Running $i
    echo =================================================
    python $i
    echo Done...
done
