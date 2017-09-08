#!/usr/bin/env bash

PYTHONPATH=$(pwd)
echo $PYTHONPATH

source activate insert-into-db-lambda
py.test -vv -r sxX
