import database.db as db
from sqlachemy import create_engine
from collector import city_dataset

engine = create_engine('postgresql://postgres:123456@localhost:5432/citizen', echo=True)

def main():
    city_dataset.columns = city_dataset.columns.str.lower()
    city_dataset.to_sql('tb_city', con=db.engine, index_label='id')

main()
