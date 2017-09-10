#!/usr/bin/env bash

source activate insert-into-db-lambda
export PYTHONPATH=$(pwd):$PYTHONPATH
py.test -vv -r sxX
