import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collector import city_dataset
from plot import dataframe_to_plot
from os import path

state = 'SP'

def main():
	df = city_dataset[city_dataset['STATE'] == state]
	df.columns = df.columns.str.lower()

	df = df[df['capital'] < 1]
	df = df[df['idhm'] > 0]
	df['carros_capita'] = df['cars'].div(df['ibge_pop'])
	df['ibge_du_capita'] = df['ibge_du'].div(df['ibge_pop'])
	df['ibge_60+_capita'] = df['ibge_60+'].div(df['ibge_pop'])

	idh = df
	idh.loc[df['idhm'] < 0.5, 'idh_class'] = 'Muito baixo'
	idh.loc[(df['idhm'] >= 0.5) & (df['idhm'] < 0.6), 'idh_class'] = 'Baixo'
	idh.loc[(df['idhm'] >= 0.6) & (df['idhm'] < 0.7), 'idh_class'] = 'Medio'
	idh.loc[(df['idhm'] >= 0.7) & (df['idhm'] < 0.8), 'idh_class'] = 'Alto'    
	idh.loc[df['idhm'] >= 0.8, 'idh_class'] = 'Muito alto'
	idh = idh[idh['idhm'] > 0]

	dataframe_to_plot(idh)

	sns.relplot(x='idhm', y='ibge_du_capita', data=df).set(
		title=f'Unidades Domésticas x IDH ({state})'
	)
	plt.show(block=True)

	sns.relplot(x='idhm', y='ibge_60+_capita', data=df).set(
		title=f'Idosos x IDH ({state})'
	)
	plt.show(block=True)

	sns.relplot(x='idhm', y='carros_capita', data=df).set(
		title=f'Carros x IDH ({state})'
	)
	plt.show(block=True)

	sns.relplot(x='idhm_renda', y='idhm_longevidade', size='idhm', hue='rural_urban', data=idh[
        (idh['rural_urban'] != '0') &
        (idh['rural_urban'] != 'Sem classificação')
    ]).set(title=f'Renda x Longevidade ({state})')
	plt.show(block=True)  

	sns.relplot(x='idhm_educacao', y='idhm_longevidade', size='idhm', hue='rural_urban', data=idh[
        (idh['rural_urban'] != '0') &
        (idh['rural_urban'] != 'Sem classificação')
    ]).set(title=f'Educação x Longevidade ({state})')
	plt.show(block=True)

	sns.relplot(x='idhm_educacao', y='idhm_renda', size='idhm', hue='rural_urban', data=idh[
        (idh['rural_urban'] != '0') &
        (idh['rural_urban'] != 'Sem classificação')
    ]).set(title=f'Educação x Renda ({state})')
	plt.show(block=True)

    # sns.countplot(x='rural_urban', hue='state', data=df[
    #     (df['rural_urban'] != '0') &
    #     (df['rural_urban'] != 'Sem classificação')
    # ]).set(title='Cidades por região')
    # plt.show(block=True)

	sns.countplot(x='rural_urban', hue='idh_class', data=df[
        (df['rural_urban'] != '0') &
        (df['rural_urban'] != 'Sem classificação')
    ]).set(title=f'Cidades por região e nivel de IDH ({state})')
	plt.show(block=True)

main()