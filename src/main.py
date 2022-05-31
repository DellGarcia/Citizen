from collector import city_dataset
from database.db import create_database

def main():
    create_database()
    print(city_dataset)

main()
