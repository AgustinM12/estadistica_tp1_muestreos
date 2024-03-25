import random

def random_array(cantidad_elegida, cantidad_poblacion):
    array = []
    while len(array) < cantidad_elegida:
        index = random.randint(0, len(cantidad_poblacion))
        if index not in array:
            array.append(index)
    return array