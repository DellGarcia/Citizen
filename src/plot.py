import matplotlib.pyplot as plt
import seaborn as sns

def dataframe_to_plot(df):
	mask1= df["long"] != 0
	mask2 = df["lat"] !=0 
	mask3 = df["idhm"] != ''

	x = df[mask1&mask2]["long"]
	y = df[mask1&mask2]["lat"]
	z = df[mask1&mask2]["idhm"]

	# hue_order = ['Muito baixo', 'Baixo', 'Medio', 'Alto', 'Muito alto']
	sns.lmplot(x="long", y="lat", data=df[mask1&mask2&mask3], fit_reg=False, hue='idh_class', legend=True, scatter_kws={"s": 30}, height=10)
	plt.show(block = True)