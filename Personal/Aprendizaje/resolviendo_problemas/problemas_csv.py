#cambiar el tipo de dato de una columna
import pandas as pd

df =pd.read_csv("resolviendo_problemas\\text.csv")

#convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#mostrar el tipo de dato del primr elemento de la columna edad
#print(type(df["edad"][0]))

#reemplazando los datos dalto por maestro
df['apellido'].replace("dalto","maestro",inplace=True)

#mostrando la columna apellido
#print(df["apellido"])

#eliminando las filas con datos vacios con axis=1 eliminan las columnas con datos faltantes
df = df.dropna()#(axis=1)

#eliminar filas repetidas
df=df.drop_duplicates()

#creando un archivo de texto con el df resultante
df.to_csv("resolviendo_problemas\\text_limpio.csv")

print(df) 