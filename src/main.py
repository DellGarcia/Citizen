import database.db as db
from sqlalchemy import create_engine
from collector import city_dataset

engine = create_engine('postgresql://postgres:123456@localhost:5432/citizen7', echo=True)

def sort_by_age_group(dataset):
    return dataset.sort_values(by=['ibge_1', 'ibge_1-4', 'ibge_5-9', 'ibge_10-14',
       'ibge_15-59', 'ibge_60+'], ascending=False)

def main():
    dataset = city_dataset
    dataset.columns = dataset.columns.str.lower()
    # Criação da tabela
    # dataset.to_sql('tb_city', con=engine, index_label='id')

    # Cidades com população mais jovem
    people_by_age_group_per_city = dataset[['city', 'state', 'ibge_1', 'ibge_1-4', 'ibge_5-9', 'ibge_10-14', 'ibge_15-59', 'ibge_60+']]
    people_by_age_group_per_city = sort_by_age_group(people_by_age_group_per_city)

    # Estados com população mais jovem
    people_by_age_group_per_state = people_by_age_group_per_city.groupby(by=['state']).sum()

    # Cidades mais populosas
    most_populated_city = dataset[['city', 'ibge_pop']].sort_values(by=['ibge_pop'], ascending=False)

    # Cidades com maior expectativa de vida para a população
    longevity_per_city = dataset[['city', 'idhm_longevidade']].sort_values(by=['idhm_longevidade'], ascending=False)
    longevity_per_city = longevity_per_city.loc[longevity_per_city['idhm_longevidade'] > 0]
    
    # Qualidade de vida melhor em cidades rurais ou urbanas
    # 1 - Rural
    best_rural_cities_to_live = dataset[['city', 'state', 'rural_urban', 'idhm']]
    best_rural_cities_to_live = best_rural_cities_to_live[best_rural_cities_to_live['rural_urban'].str.contains('Rural')].sort_values(by=['idhm'], ascending=False)

    # 2 - Urbano
    best_urban_cities_to_live = dataset[['city', 'state', 'rural_urban', 'idhm']]
    best_urban_cities_to_live = best_urban_cities_to_live[best_urban_cities_to_live['rural_urban'].str.contains('Urban')].sort_values(by=['idhm'], ascending=False)

    print(best_urban_cities_to_live.head(20))

main()
