import datetime as dt

from sqlalchemy import Column, DateTime, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base


def prepare_event_to_insert(event_data, table_name):
    """
    Given a dictionary, it extract the needed attributes and return an SQL Alchemy object ready
    to insert in a database
    :param data: dict data to insert
    :param table_name: string name of the table where to insert
    :return:
    """
    base = declarative_base()

    class GenericEvent(base):
        __tablename__ = table_name
        __table_args__ = {'extend_existing': True}
        id = Column(Integer, primary_key=True)
        insert_date_sk = Column(Integer)
        insert_timestamp = Column(DateTime)
        name = Column(String)
        description = Column(String)

    # redefine time
    insert_timestamp = dt.datetime.now()
    insert_date_sk = int(insert_timestamp.strftime('%Y%m%d'))

    event = GenericEvent(
        insert_date_sk=insert_date_sk,
        insert_timestamp=insert_timestamp,
        name=event_data['name'],
        description=event_data['description']
    )

    return event
