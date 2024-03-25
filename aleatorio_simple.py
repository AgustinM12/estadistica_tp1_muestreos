import json
import random
import statistics
from funcion_ayuda import random_array as ra

(open("edades.json"))

poblacion = json.load(open("edades.json")) 

def muestreo_aleatorio_probabilistico(cantidad_muestra, cantidad_poblacion):
    if cantidad_muestra < len(cantidad_poblacion):
        muestra = []

        list_index = ra(cantidad_muestra, cantidad_poblacion)

        for _i in range(0, len(cantidad_poblacion)):
            if _i in list_index:
                muestra.append(cantidad_poblacion[_i]["age"])

        print("La muestra es de ", len(list_index), " individuos son: ", list_index)

        print("El promedio de las edades es: ", statistics.mean(muestra))
    else:
        print("La muestra debe ser menor a la poblacion")

muestreo_aleatorio_probabilistico(26, poblacion)