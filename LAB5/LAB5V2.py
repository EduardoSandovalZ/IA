import numpy as np

# Definir los pesos iniciales de la red neuronal
weights = np.array([0.5, 0.5, 0.5])

# Función de activación (función escalón)
def activation_function(x):
    if x < 0:
        return 0
    else:
        return 1

# Función para clasificar los libros
def classify_books(weight, freq):
    # Crear el vector de entrada
    x = np.array([1, weight, freq])

    # Calcular la salida de la red neuronal
    output = activation_function(np.dot(x, weights))

    # Clasificar el libro en uno de los 4 conjuntos
    if weight <= 2 and freq <= 5:
        if output == 0:
            return "Ligero y poco usado - Conjunto 1"
        else:
            return "Ligero y poco usado - Conjunto 2"
    elif weight <= 2 and freq > 5:
        if output == 0:
            return "Ligero y muy usado - Conjunto 3"
        else:
            return "Ligero y muy usado - Conjunto 4"
    elif weight > 2 and freq <= 5:
        if output == 0:
            return "Pesado y poco usado - Conjunto 1"
        else:
            return "Pesado y poco usado - Conjunto 2"
    else:
        if output == 0:
            return "Pesado y muy usado - Conjunto 3"
        else:
            return "Pesado y muy usado - Conjunto 4"

# Ejemplo de uso
weight = float(input("Ingrese el peso del libro (en kilogramos): "))
freq = int(input("Ingrese la frecuencia de uso del libro (en préstamos por mes): "))

print(classify_books(weight, freq))

'''
En este código, primero definimos los pesos iniciales de la red neuronal (en este caso, 0.5 para cada uno de los 3 pesos), 
y la función de activación, que en este caso es la función escalón. 
Luego, definimos la función classify_books que toma como entrada el peso y la frecuencia de uso de un libro, 
y devuelve una cadena indicando a qué conjunto pertenece.

En el ejemplo de uso, el programa le pide al usuario que ingrese el peso y la frecuencia de uso de un libro, 
y luego utiliza la función classify_books para clasificar el libro en uno de los 4 conjuntos.
'''
