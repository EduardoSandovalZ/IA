import numpy as np
import matplotlib.pyplot as plt

num_libros = 8
libros = [[0.7,3],[1.5,5],[2.0,9],[0.9,11],[4.2,0],[2.2,1],[3.6,7],[4.5,6]]

data = np.array(libros)
X = (data - data.mean(axis=0)) / data.std(axis=0)

class Adaline:
    def __init__(self, input_size, output_size):
        self.input_size = input_size
        self.output_size = output_size
        self.weights = np.random.randn(input_size, output_size) * 0.01

    def predict(self, X):
        return X @ self.weights
    
    def train(self, X, y, epochs, lr):
        for epoch in range(epochs):
            output = self.predict(X)
            self.weights += lr * X.T @ (y - output)

adaline = Adaline(input_size=2, output_size=4)
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

adaline.train(X, y, epochs=1000, lr=0.01)
conjuntos = np.argmax(adaline.predict(X), axis=1)
conjuntos_nombre = {0: "Ligeros y poco usados", 1: "Ligeros y muy usados", 2: "Pesados y poco usados", 3: "Pesados y muy usados"}
for i, conjunto in enumerate(conjuntos):
    print(f"El libro {i+1} con peso {data[i][0]:.2f} y frecuencia {data[i][1]:.2f} pertenece al conjunto '{conjuntos_nombre[conjunto]}'.")

plt.figure(figsize=(8, 6))
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.01),np.arange(y_min, y_max, 0.01))
Z = np.argmax(adaline.predict(np.c_[xx.ravel(), yy.ravel()]), axis=1)
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, alpha=0.4)

colores = ['blue', 'red', 'green', 'purple']

plt.scatter(X[:, 0], X[:, 1], c=[colores[c] for c in conjuntos])

for i in range(4):
    
    plt.scatter([], [], c=colores[i], label=conjuntos_nombre[i])
plt.legend()
plt.title("Clasificación de libros")
plt.xlabel("Peso")
plt.ylabel("Frecuencia")
plt.show()

