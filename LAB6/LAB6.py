import numpy as np
from prettytable import PrettyTable
#Creamos la clase perceptron
class Perceptron:
    #Creamos el constructor
    def __init__(self, input_size, output_size):
        #Entradas
        self.input_size = input_size
        #Salidas
        self.output_size = output_size
        #Instanciamos los pesos
        self.weights = np.random.rand(input_size, output_size)
        #Instanciamos el BIAS
        self.bias = np.random.rand(output_size)
    #Creamos la funcion predict la cual recibe el vector X 
    def predict(self, X):
        #Devuelve devulve el vector X ya tomando en cuenta los pesos y el bias
        return np.argmax(X @ self.weights + self.bias, axis=1)
    #Funcion de entrenamiento, recibe el vector de entrada, el valor deseado de salida, el num de iteraciones y la curva de aprendizaje
    def train(self, X, y, epochs, lr):
        #Creamos un arreglo donde guardamos los errores
        errors = []
        #Iteramos n veces
        for epoch in range(epochs):
            #Obtenemos la salida en base a las entradas, los pesos y el bias
            output = X @ self.weights + self.bias
            #Calculamos el error
            error = y - output
            #Calculamos los nuevos pesos en base al error
            self.weights += lr * X.T @ error
            #Recalculamos el valor del bias
            self.bias += lr * np.sum(error, axis=0)
            #Guardamos el error obtenido en el arreglo
            errors.append(np.mean(np.abs(error)))
        #Devolvemos el error
        return errors
#Metodo para verificar si son pares o impares
def get_labels_pares(datos):
    #Creamos un vector con 0 inicializados
    y = np.zeros((datos.shape[0], 1))
    #Recorremos el arreglo de datos
    for i, row in enumerate(datos):
        #Verificamos Que el elemento sea par
        if row[0] % 2 == 0:
            y[i] = 1
    return y
#Funcion para determinar si son mayores a 5
def get_labels_mayores_a_5(datos):
    #Creamos un vector con 0 inicializados
    y = np.zeros((datos.shape[0], 1))
    #Recorremos el arreglo de datos
    for i, row in enumerate(datos):
        #Verificamos Que el elemento sea mayor a 5
        if row[0] > 5:
            y[i] = 1
    return y
#Funcion para determinar si son primos
def get_labels_primos(datos):
    #Creamos un vector con 0 inicializados
    y = np.zeros((datos.shape[0], 1))
    #Recorremos el arreglo de datos
    for i, row in enumerate(datos):
        #Verificamos Que el elemento sea primo
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
