from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

def save_new_member(name, age):
    engine = create_engine("postgresql+psycopg2://tester:1111@localhost/tester", echo=True)
    meta = MetaData()

    my_family = Table(
        'my_family', meta,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('age', Integer)
    )

    meta.create_all(engine)
    conn = engine.connect()

    ins = my_family.insert().values(
        name=name,
        age=age
    )
    conn.execute(ins)
