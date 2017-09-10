import os

import pytest

from src.helpers import get_db_string


def test_connection_string_with_no_env():
    with pytest.raises(KeyError):
        connection_string = get_db_string()
        pass


def test_connection_string():
    os.environ['DB_HOSTNAME'] = 'test'
    os.environ['DB_NAME'] = 'test'
    os.environ['DB_USER'] = 'test'
    os.environ['DB_PASSWORD'] = 'test'

    connection_string = get_db_string()
    comparison_sting = 'postgresql://test:test@test:5432/test'
    assert connection_string == comparison_sting
