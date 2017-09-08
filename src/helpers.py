import os


def get_db_string():
    """
    Extract env variables to connect to DB and return a db string
    Raise an error if the env variables are not set
    :return: string
    """
    db_hostname = os.environ['DB_HOSTNAME']
    db_name = os.environ['DB_NAME']
    db_user = os.environ['DB_USER']
    db_password = os.environ['DB_PASSWORD']
    db_connection_string = f'postgresql://{db_user}:{db_password}@{db_hostname}:5432/{db_name}'
    return db_connection_string
