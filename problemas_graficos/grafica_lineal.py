import pandas as pd
#libreria de visualizacion de datos
import matplotlib.pyplot as plt
import seaborn as sns

df =pd.read_csv("problemas_graficos\\pedos.csv")

#creando grafica con los datos
sns.lineplot(x = "fecha", y="pedos", data=df)

#creando un punto en el momento de mas pedos
plt.plot("02-02",23,"o")

plt.show()