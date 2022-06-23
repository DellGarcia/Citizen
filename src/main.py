import database.db as db
from sqlalchemy import create_engine
from collector import city_dataset
from plot import dataframe_to_plot

engine = create_engine('postgresql://postgres:123456@localhost:5432/citizen7', echo=True)

def sort_by_age_group(df):
    return df.sort_values(by=['ibge_1', 'ibge_1-4', 'ibge_5-9', 'ibge_10-14',
       'ibge_15-59', 'ibge_60+'], ascending=False)

def main():
    df = city_dataset
    df.columns = df.columns.str.lower()
    # Criação da tabela
    # df.to_sql('tb_city', con=engine, index_label='id')

    # Cidades com população mais jovem
    people_by_age_group_per_city = df[['city', 'state', 'ibge_1', 'ibge_1-4', 'ibge_5-9', 'ibge_10-14', 'ibge_15-59', 'ibge_60+']]
    people_by_age_group_per_city = sort_by_age_group(people_by_age_group_per_city)

    # Estados com população mais jovem
    people_by_age_group_per_state = people_by_age_group_per_city.groupby(by=['state']).sum()

    # Cidades mais populosas
    most_populated_city = df[['city', 'ibge_pop']].sort_values(by=['ibge_pop'], ascending=False)

    # Cidades com maior expectativa de vida para a população
    longevity_per_city = df[['city', 'idhm_longevidade']].sort_values(by=['idhm_longevidade'], ascending=False)
    longevity_per_city = longevity_per_city.loc[longevity_per_city['idhm_longevidade'] > 0]
    
    # Qualidade de vida melhor em cidades rurais ou urbanas
    # 1 - Rural
    best_rural_cities_to_live = df[['city', 'state', 'rural_urban', 'idhm']]
    best_rural_cities_to_live = best_rural_cities_to_live[best_rural_cities_to_live['rural_urban'].str.contains('Rural')].sort_values(by=['idhm'], ascending=False)

    # 2 - Urbano
    best_urban_cities_to_live = df[['city', 'state', 'rural_urban', 'idhm']]
    best_urban_cities_to_live = best_urban_cities_to_live[best_urban_cities_to_live['rural_urban'].str.contains('Urban')].sort_values(by=['idhm'], ascending=False)

    # Exportando cidades rurais e urbanas
    # df[df['rural_urban'].str.contains('Rural')].to_excel("rural.xlsx")
    # df[df['rural_urban'].str.contains('Urban')].to_excel("urban.xlsx")

    low_idh = df[df['idhm'] < 0.499]
    high_idh = df[df['idhm'] >= 0.800]
    medium_idh = df[(df['idhm'] > 0.499) & (df['idhm'] < 0.800)]

    idh = df
    idh.loc[df['idhm'] < 0.5, 'idh_class'] = 'Muito baixo'
    idh.loc[(df['idhm'] >= 0.5) & (df['idhm'] < 0.6), 'idh_class'] = 'Baixo'
    idh.loc[(df['idhm'] >= 0.6) & (df['idhm'] < 0.7), 'idh_class'] = 'Medio'
    idh.loc[(df['idhm'] >= 0.7) & (df['idhm'] < 0.8), 'idh_class'] = 'Alto'    
    idh.loc[df['idhm'] >= 0.8, 'idh_class'] = 'Muito alto'

    # dataframe_to_plot(idh)

    sp = df[df['state'].str.contains('PE')]
    #sp.to_excel('mg.xlsx')

    dataframe_to_plot(sp)

    # low_idh.to_excel('low_idh.xlsx')
    # medium_idh.to_excel('medium_idh.xlsx')
    # high_idh.to_excel('high_idh.xlsx')

    

main()
