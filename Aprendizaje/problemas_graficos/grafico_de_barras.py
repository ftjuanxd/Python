import pandas as pd
#libreria de visualizacion de datos
import matplotlib.pyplot as plt
import seaborn as sns#para usarlo toca instalarlos pero mi computdor fallo empezo a fallar

df =pd.read_csv("problemas_graficos\\ingresos.csv")

#creando grafica con los datos
sns.barplot(x ="fuente", y="ingresos", data=df)

#obteniendo el total de ingresos
total_ingresos = df["ingresos"],sum()

#mostrando el total
print(f"El total de ingresos es de: ${total_ingresos} USD")

#mostrando tabla
plt.show()