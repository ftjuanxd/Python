import pandas as pd
#dataframe estructucra de datos parecida a hojas de calculo
#usando la funcion read_csv para leer el archivo csv y cambiando el nombre de los encabezados de las columnas
df = pd.read_csv("archivos\\text.csv")#,names=["name","lastname","age"]
df2 =pd.read_csv("archivos\\text.csv")#,names=["name","lastname","age"]


#obteniendo los datos de la columna nombre
nombres = df["nombre"]

#ordenando la data frame por la edad
df_ordenado_ascendente = df.sort_values("edad")

#ordenando la data frame por la edad de forma descendente
df_ordenado_descendente = df.sort_values("edad",ascending=False)

#concatenando los dos date frame 
df_concatenado = pd.concat([df,df2])

#accediendo a las primeras filas con head solo cambiaar el valor del cero por el numero hasta donde se quiere mostrar
primeras_filas= df.head(0)

#accediendo a las ultimas 3 filas con tail()
ultimas_filas = df.tail(3)

#accediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales =df.shape

#obteniendo data estadistica del data frame
df_info = df.describe()

#accediendo a la edad de  la fila 2 
elemento_especifico_loc = df.loc[2,"edad"]

#accediendo a la edad de  la fila 2 con iloc 
elemento_especifico_iloc = df.iloc[2,2]

#accediendo a todas las filas de una columna con loc
apellidos =  df.loc[:,"apellido"]

#accediendo a todas las filas de una columna con iloc
apellidos =  df.iloc[:,1]

#accediendoa la fila 3 con loc
fila_3 = df.loc[2,:]

#accediendoa la fila 3 con iloc
fila_3 = df.iloc[2,:]

#accediendo a filas con edad mayor que 30
mayor_que_30 =  df.loc[df["edad"]>30,:]

#accediendo a filas con edad menor que 30
menor_que_30 =  df.loc[df["edad"]<30,:]

print(mayor_que_30)