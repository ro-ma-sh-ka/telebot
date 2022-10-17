from sqlalchemy import create_engine, Column, Integer, String, Date, MetaData, Table, \
    DateTime, Date
from datetime import datetime


def create_table():
    engine = create_engine("postgresql+psycopg2://tester:1111@localhost/tester", echo=True)
    meta = MetaData()

    my_family = Table(
        'my_family', meta,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('name', String(20), nullable=False),
        Column('surname', String(30), nullable=True),
        Column('birthday', Date, nullable=False),
        Column('created_on', DateTime, default=datetime.now)
    )

    meta.create_all(engine)
    engine.connect()
