import logging
import os

import pandas as pd
from sqlalchemy import create_engine

from helpers import get_db_string

logger = logging.getLogger()
logger.setLevel(logging.INFO)

logger.info('Loading function')


def lambda_handler(event, context):
    logger.info(event)
    logger.info(context)
    connection_string = get_db_string()
    postgres_engine = create_engine(connection_string)

    tables = pd.read_sql('SELECT * FROM pg_catalog.pg_tables;', con=postgres_engine)
    logger.info(tables)
    return event
