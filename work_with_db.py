from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, \
    Date, DateTime
from datetime import datetime


def create_table():
    engine = create_engine("postgresql+psycopg2://tester:1111@localhost/tester", echo=True)
    meta = MetaData()

    Table(
        'my_family', meta,
        Column('id', Integer, primary_key=True),
        Column('name', String(20), nullable=False),
        Column('surname', String(30), nullable=True),
        Column('birthday', Date, nullable=False),
        Column('created_on', DateTime, default=datetime.now)
    )

    meta.create_all(engine)
    engine.connect()

def check_is_exist(name, age):
    pass


def save_new_member(name, surname, birthday, created_on):
    # connect to DB
    engine = create_engine("postgresql+psycopg2://tester:1111@localhost/tester", echo=True)
    # create an engine
    meta = MetaData(engine)
    # Connect table
    my_table = Table('my_family', meta, autoload=True)
    # get connection
    conn = engine.connect()
    # send a data
    conn.execute(my_table.insert(), name=name, surname=surname, birthday=birthday, created_on=created_on)


def family_list():
    engine = create_engine("postgresql+psycopg2://tester:1111@localhost/tester", echo=True)
    meta = MetaData(engine)
    my_table = Table('my_family', meta, autoload=True)
    conn = engine.connect()
    my_select = conn.execute(my_table.select())
    my_list =[]
    for row in my_select:
        my_list.append(row)
    return my_list

