import pandas as pd
#libreria de visualizacion de datos
import matplotlib.pyplot as plt
import seaborn as sns

df =pd.read_csv("problemas_graficos\\bigotes.csv")

#creando grafica con los datos
sns.boxplot(x ="categoria", y="valor", data=df)

#mostrando tabla
plt.show()