import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn_som.som import SOM
from collector import city_dataset

city_dataset.columns = city_dataset.columns.str.lower()

city_dataset = city_dataset[city_dataset['state'] == 'SP']

cities = city_dataset['city']
lat = city_dataset['lat']
log = city_dataset['long']

data = city_dataset[['cars', 'motorcycles', 'ibge_pop', 'idhm', 'ibge_60+' , 'ibge_du', 'pay_tv', 'fixed_phones', 'gdp_capita']]

df = pd.DataFrame()
df['carros_capita'] = data['cars'].div(data['ibge_pop'])
df['motos_capita'] = data['motorcycles'].div(data['ibge_pop'])
df['ibge_du_capita'] = data['ibge_du'].div(data['ibge_pop'])
df['ibge_60+_capita'] = data['ibge_60+'].div(data['ibge_pop'])
df['tv_du'] = data['pay_tv'].div(data['ibge_du'])
df['fixed_phones_du'] = data['fixed_phones'].div(data['ibge_du'])

df = df.head(1000).to_numpy()

# Crio uma SOM com 5x1 neurônios (5 clusters)
som = SOM(m=3, n=1, dim=6, random_state=1234)

# Busca de agrupamentos
som.fit(df)

# Associo cada país com o grupo respectivo
predictions = som.predict(df)

dic = {}
for i,p in enumerate(predictions):
  if p in dic.keys():
    dic[p].append(cities.iloc[i])
  else: dic[p] = [cities.iloc[i]]

for i in dic.keys():
  lista = dic[i]
  print(sorted(lista))
  print('---------------------------------\n\n')

df2 = data
df2['city'] = cities
df2['cluster'] = predictions


mask1= log != 0
mask2 = lat !=0 


df2['lat'] = lat
df2['long'] = log


# hue_order = ['Muito baixo', 'Baixo', 'Medio', 'Alto', 'Muito alto']
sns.lmplot(x="long", y="lat", data=df2[mask1&mask2], fit_reg=False, hue='cluster', legend=True, scatter_kws={"s": 30}, height=10)
plt.show(block = True)