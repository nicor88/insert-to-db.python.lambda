[![Build Status](https://travis-ci.org/nicor88/insert-to-db.python.lambda.svg?branch=master)](https://travis-ci.org/nicor88/insert-to-db.python.lambda)

# insert-to-db.python.lambda
Generic AWS lambda to insert an event to a Postgres Database (for now)

## Local development
It's possible to use VIRTUALENV or create a conda environment

<pre>conda create --name insert-into-db-lambda python=3.6
source activate insert-into-db-lambda
</pre>

## Install Libs
<pre>pip install pytest
pip install -r requirements.txt
</pre>

## Run tests
`py.test -vv -r sxX`
or
`make run_tests` (it only works if you have a conda env called `insert-into-db-lambda`)

## AWS Setup
Requirements:
* Handler: `lambda_function.lambda_handler`
* Runtime: `python3.6`
* Environment variables:
  * `DB_USER`
  * `DB_PASSWORD`
  * `DB_HOSTNAME`
  * `DB_NAME`
