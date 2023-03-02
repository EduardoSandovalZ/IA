import numpy as np
import matplotlib.pyplot as plt

num_libros = 8
libros = [[0.7,3],[1.5,5],[2.0,9],[0.9,11],[4.2,0],[2.2,1],[3.6,7],[4.5,6]]

'''
libros = []
    for i in range(num_libros):
    peso = np.random.uniform(0.5, 5.0)
    frecuencia = np.random.uniform(1, 10)
    libros.append([peso, frecuencia])
    
'''


data = np.array(libros)
X = (data - data.mean(axis=0)) / data.std(axis=0)

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
conjuntos = perceptron.predict(X)
conjuntos_nombre = {0: "Ligeros y poco usados", 1: "Ligeros y muy usados", 2: "Pesados y poco usados", 3: "Pesados y muy usados"}
for i, conjunto in enumerate(conjuntos):
    print(f"El libro {i+1} con peso {data[i][0]:.2f} y frecuencia {data[i][1]:.2f} pertenece al conjunto '{conjuntos_nombre[conjunto]}'.")


plt.figure(figsize=(8, 6))
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),np.arange(y_min, y_max, 0.1))
Z = perceptron.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.4)
plt.scatter(X[:, 0], X[:, 1], c=conjuntos)
for i in range(4):
    plt.scatter([], [], c='C{}'.format(i), label=conjuntos_nombre[i])
plt.legend()
plt.title("Clasificación de libros")
plt.xlabel("Peso")
plt.ylabel("Frecuencia")
plt.show()



