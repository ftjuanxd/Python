import pandas as pd
#libreria de visualizacion de datos
import matplotlib.pyplot as plt
import seaborn as sns

df =pd.read_csv("problemas_graficos\\dispersion.csv")

#creando grafica con los datos
sns.scatterplot(x ="tiempo", y="dinero", data=df)

#mostrando tabla
plt.show()