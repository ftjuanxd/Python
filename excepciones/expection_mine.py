#creando mi propia excepcion 
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Impresionante cometiste el siguiente error: {err}")
    
#lanzando mi propia excepcion   
#raise MiExcepcion("Que boludo diviste por cero")

#manejando mi propia excepcion
try: 
    raise MiExcepcion("Que boludo diviste por cero")
except:
    print("como vas a cometer ese error")
    

