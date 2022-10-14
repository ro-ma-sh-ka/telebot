from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, insert, select


def create_table():
    engine = create_engine("postgresql+psycopg2://tester:1111@localhost/tester", echo=True)
    meta = MetaData()

    Table(
        'my_family', meta,
        Column('id', Integer, primary_key=True),
        Column('name', String(20)),
        Column('surname', String(30)),
        Column('age', Integer)
    )

    meta.create_all(engine)
    engine.connect()


def check_is_exist(name, age):
    pass


def save_new_member(name, age):
    # connect to DB
    engine = create_engine("postgresql+psycopg2://tester:1111@localhost/tester", echo=True)
    # create an engine
    meta = MetaData(engine)
    # Connect table
    my_table = Table('my_family', meta, autoload=True)
    # get connection
    conn = engine.connect()
    # send a data
    conn.execute(my_table.insert(), name=name, age=age)


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

