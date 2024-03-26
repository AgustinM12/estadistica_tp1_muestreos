import random
import json

poblacion = json.load(open("edades.json"))

def random_array(cantidad_elegida, cantidad_poblacion):
    array = []
    while len(array) < cantidad_elegida:
        index = random.randint(0, len(cantidad_poblacion))
        if index not in array:
            array.append(index)
    return array

def sistematic_array(inicio, salto, cantidad_elegida, cantidad_poblacion):
    array = []
    count = inicio

    while len(array) < cantidad_elegida:
        if count not in array:
            array.append(count)
        count += salto
        if count + salto >= len(cantidad_poblacion):
            inicio += 1
            count = inicio
    return array


#print("Random array", random_array(26,poblacion))
xd = sistematic_array(0,5,26,poblacion)
print("Sistematic array", xd)
print(len(xd))