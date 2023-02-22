import numpy as np

# Paso 1: Solicitar al usuario que ingrese los datos de los libros

num_libros = 20
libros = []
for i in range(num_libros):
    peso = np.random.uniform(0.5, 5.0)
    frecuencia = np.random.uniform(1, 10)
    libros.append([peso, frecuencia])

# Paso 2: Crear un array con los datos de los libros
data = np.array(libros)

# Paso 3: Normalizar las características para que tengan una media de cero y una desviación estándar de uno
X = (data - data.mean(axis=0)) / data.std(axis=0)

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
for i, row in enumerate(data):
    if row[0] <= 2 and row[1] <= 5:
        y[i][0] = 1
    elif row[0] <= 2 and row[1] >= 5:
        y[i][1] = 1
    elif row[0] > 2 and row[1] <= 5:
        y[i][2] = 1
    else:
        y[i][3] = 1
perceptron.train(X, y, epochs=100, lr=0.01)

# Paso 6: Usar la red neuronal para clasificar los libros según su peso y frecuencia de uso
conjuntos = perceptron.predict(X)

# Paso 7: Asignar cada conjunto a los libros según su peso y frecuencia de uso
conjuntos_nombre = {0: "Ligeros y poco usados", 1: "Ligeros y muy usados", 2: "Pesados y poco usados", 3: "Pesados y muy usados"}
for i, conjunto in enumerate(conjuntos):
    print(f"El libro {i+1} con peso {data[i][0]:.2f} y frecuencia {data[i][1]:.2f} pertenece al conjunto '{conjuntos_nombre[conjunto]}'.")

