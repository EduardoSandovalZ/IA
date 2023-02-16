import numpy as np
import pandas as pd

# Paso 1: Solicitar al usuario que ingrese los datos de los libros
num_libros = int(input("Ingrese el número de libros que desea clasificar: "))
libros = []
for i in range(num_libros):
    peso = float(input(f"Ingrese el peso del libro {i+1}: "))
    frecuencia = float(input(f"Ingrese la frecuencia de uso del libro {i+1}: "))
    libros.append([peso, frecuencia])

# Paso 2: Crear un DataFrame con los datos de los libros
data = pd.DataFrame(libros, columns=["peso", "frecuencia"])

# Paso 3: Normalizar las características para que tengan una media de cero y una desviación estándar de uno
X = (data - data.mean()) / data.std()

# Paso 4: Definir la arquitectura de la red neuronal perceptrón
class Perceptron:
    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size
        self.weights = np.random.rand(input_size, output_size)

    def predict(self, X):
        return np.argmax(X @ self.weights, axis=1)

    def train(self, X, y, epochs, lr):
        for epoch in range(epochs):
            output = X @ self.weights
            error = y - output
            self.weights += lr * X.T @ error

# Paso 5: Crear una instancia de la red neuronal perceptrón y entrenarla con los datos
perceptron = Perceptron(input_size=2, output_size=4)
y = np.zeros((num_libros, 4))
for i, row in data.iterrows():
    if row["peso"] <= 2 and row["frecuencia"] <= 5:
        y[i][0] = 1
    elif row["peso"] <= 2 and row["frecuencia"] > 5 and row["frecuencia"] < 10:
        y[i][1] = 1
    elif row["peso"] > 2 and row["peso"] <= 5 and row["frecuencia"] <= 5:
        y[i][2] = 1
    else:
        y[i][3] = 1
perceptron.train(X.to_numpy(), y, epochs=100, lr=0.01)

# Paso 6: Usar la red neuronal para clasificar los libros según su peso y frecuencia de uso
conjuntos = perceptron.predict(X.to_numpy())

# Paso 7: Asignar cada conjunto a los libros según su peso y frecuencia de uso
conjuntos_nombre = {0: "Ligeros y poco usados", 1: "Ligeros y muy usados", 2: "Pesados y poco usados", 3: "Pesados y muy usados"}
for i, conjunto in enumerate(conjuntos):
    print(f"El libro {i+1} pertenece al conjunto '{conjuntos_nombre[conjunto]}'.")
