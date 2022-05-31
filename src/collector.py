import pandas as pd
from os import path

full_path = path.join(path.dirname(__file__), '..', 'data', 'BRAZIL_CITIES_REV2022.csv')
city_dataset = pd.read_csv(full_path)
