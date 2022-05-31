from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

def create_database():
    engine = create_engine('postgresql://postgres:123456@localhost:5432/citizen', echo=True)

    base = declarative_base()

    declare_models(base)

    base.metadata.create_all(engine)

def declare_models(base):
     class City (base):
        __tablename__ = 'tb_city'

        id = Column(Integer, primary_key=True)
        name = Column(String(50))