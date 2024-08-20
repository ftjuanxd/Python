import pandas as pd
#forma de cargar grande conjunto de datos
def read_csv_in_chunks(file_name):
    for i, chunck in enumerate(pd.read_csv(file_name,chunksize=1000)):
        print("Chunk # {}".format(i))
        print(chunck)
    
read_csv_in_chunks("problemas_graficos\\pedos.csv")