from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session
from models import declare_models
from pandas import DataFrame

engine = create_engine('postgresql://postgres:123456@localhost:5432/citizen4', echo=True)

base = declarative_base()

def create_database():
    declare_models(base)

    base.metadata.create_all(engine)

def insert_dataframe(df: DataFrame):
    df.reset_index()

    with Session(engine) as session:
        

        spongebob = User()
        session.add_all([spongebob, sandy, patrick])
        session.commit()

    for index, row in df.iterrows():
        print(row['STATE'])
