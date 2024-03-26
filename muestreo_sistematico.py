import json 
import statistics
from funcion_indices import sistematic_array as sa

poblacion = json.load(open("edades.json"))

def muestreo_aleatorio_sistematico(inicio, salto, cantidad_muestra, poblacion_datos):

    if cantidad_muestra < len(poblacion_datos):
        muestra = []
        
        list_index = sa(inicio,salto,cantidad_muestra,poblacion_datos)

        for _i in range(0, len(poblacion_datos)):
            if _i in list_index:
                muestra.append(poblacion_datos[_i]["age"])

        print("La muestra es de ", len(list_index), " individuos tienen las edades: ", muestra)

        print("El promedio de las edades es: ", statistics.mean(muestra))

muestreo_aleatorio_sistematico(1,5,26, poblacion)
