import numpy as np
from prettytable import PrettyTable

class Perceptron:
    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size
        self.weights = np.random.rand(input_size, output_size)
        self.bias = np.random.rand(output_size)

    def predict(self, X):
        return np.argmax(X @ self.weights + self.bias, axis=1)
    
    def train(self, X, y, epochs, lr):
        errors = []
        for epoch in range(epochs):
            output = X @ self.weights + self.bias
            error = y - output
            self.weights += lr * X.T @ error
            self.bias += lr * np.sum(error, axis=0)
            errors.append(np.mean(np.abs(error)))
        return errors

def get_labels_pares(datos):
    y = np.zeros((datos.shape[0], 1))
    for i, row in enumerate(datos):
        if row[0] % 2 == 0:
            y[i] = 1
    return y

def get_labels_mayores_a_5(datos):
    y = np.zeros((datos.shape[0], 1))
    for i, row in enumerate(datos):
        if row[0] > 5:
            y[i] = 1
    return y

def get_labels_primos(datos):
    y = np.zeros((datos.shape[0], 1))
    for i, row in enumerate(datos):
        if row[0] in [2, 3, 5, 7]:
            y[i] = 1
    return y

# Datos de entrada para los tres casos
datos = np.array([[1, 1, 1, 0, 1, 1, 1],  # 0
                  [0, 0, 1, 0, 0, 1, 0],  # 1
                  [1, 0, 1, 1, 1, 0, 1],  # 2
                  [1, 0, 1, 1, 0, 1, 1],  # 3
                  [0, 1, 1, 1, 0, 1, 0],  # 4
                  [1, 1, 0, 1, 0, 1, 1],  # 5
                  [1, 1, 0, 1, 1, 1, 1],  # 6
                  [1, 0, 1, 0, 0, 1, 0],  # 7
                  [1, 1, 1, 1, 1, 1, 1],  # 8
                  [1, 1, 1, 1, 0, 1, 1]]) # 9

# Normalización de los datos
X = datos.astype(float)
X /= X.max()

# Selección del caso
caso = 1

if caso == 1:
    # Caso 1: detectar dígitos pares
    y = get_labels_pares(datos)
elif caso == 2:
    # Caso 2: detectar números mayores a 5
    y = get_labels_mayores_a_5(datos)
elif caso == 3:
    # Caso 3: detectar números primos
    y = get_labels_primos(datos)
else:
    print("Caso no válido")

model = Perceptron(input_size=X.shape[1], output_size=1)
errors = model.train(X, y, epochs=1000, lr=0.01)

table = PrettyTable()

# Imprimir los pesos finales y el bias
table = PrettyTable()
table.field_names = ["Pesos finales"]
for i in range(model.weights.shape[0]):
    table.add_row([model.weights[i]])
print(table)

table = PrettyTable()
table.field_names = ["Bias final"]
table.add_row([model.bias])
print(table)

# Imprimir los errores por época
table = PrettyTable()
table.field_names = ["Epoch", "Error"]
for i in range(len(errors)):
    table.add_row([i+1, errors[i]])
print(table)
