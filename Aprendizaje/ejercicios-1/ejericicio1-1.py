#promedio de duracion
otros_cursos_min=2.5
otros_cursos_max=7
otros_cursos_promedio=4
este_curso = 1.5

#duracion de crudos
crudo_promedio =  5
este_crudo = 3.5

#diferencias de duracion
diferencia_con_min= 100 - este_curso / otros_cursos_min * 100
diferencia_con_max= 100 - este_curso * 1000 // otros_cursos_max / 10
diferencia_con_promedio= 100 - este_curso /otros_cursos_promedio * 100

#calculando el porcentaje de tiempo vacio recorrido
tiempo_vacio_promedio= 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10

tiempo_vacio_este= 100 - este_curso * 1000 // este_crudo / 10
print("-------------------------------")
print(f'Este curso dura un {diferencia_con_min} % menos que el mas rapido')
print(f' - un {diferencia_con_max} % menos que el mas lento')
print(f' - un {diferencia_con_promedio} % menos que el promedio')
print("-------------------------------")
#mostrando la cantidad de espacios vacions que se remueven (ejercicio B)
print(f'un curso promedio elimina: {tiempo_vacio_promedio} % de tiempo vacio')
print(f'este curso elimina: {tiempo_vacio_este} % de tiempo vacio')
print("-------------------------------")
#mostrando diferenccias si los cursos duraran 10 horas
print(f'Ver 10 horas de este curso equivale a ver { otros_cursos_promedio * 100 // este_curso / 10} horas de otros cursos')

print(f'Ver 10 horas de este curso equivale a ver { este_curso * 100 // otros_cursos_promedio / 10} horas de otros cursos')