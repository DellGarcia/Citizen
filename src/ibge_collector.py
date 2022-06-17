import pandas as pd
from os import path


full_path = path.join(path.dirname(__file__), '..', 'data', 'subdistritos.csv')
ibge_dataset = pd.read_csv(full_path)

print(ibge_dataset)
