# insert-to-db.python.lambda
Generic AWS lambda to insert an event to a Postgres Database (for now)

## Conda env for local development
<pre>
conda create --name insert-into-db-lambda python=3.6
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
