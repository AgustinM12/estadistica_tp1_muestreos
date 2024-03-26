import json
import statistics
from funcion_indices import random_array as ra

poblacion = json.load(open("edades.json")) 

def muestreo_aleatorio_probabilistico(cantidad_muestra, poblacion_datos):
    if cantidad_muestra < len(poblacion_datos):
        muestra = []

        list_index = ra(cantidad_muestra, poblacion_datos)

        for _i in range(0, len(poblacion_datos)):
            if _i in list_index:
                muestra.append(poblacion_datos[_i]["age"])

        print("La muestra es de ", len(list_index), " individuos son: ", list_index)

        print("El promedio de las edades es: ", statistics.mean(muestra))
    else:
        print("La muestra debe ser menor a la poblacion")

muestreo_aleatorio_probabilistico(26, poblacion)