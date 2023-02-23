import numpy as np
import matplotlib.pyplot as plt
# numero de libros que vamos a clasificar libros
num_libros = 20
#generamos una lista donde almacenaremos los libros
libros = []
#Recorremos la lista de libros 
for i in range(num_libros):
    #Asignamos un peso aleatorio en un rango de 0.5 a 5 kg
    peso = np.random.uniform(0.5, 5.0)
    #Asignamos una frecuencia de retiro mensual aleatoria en un rango de 1 a 10 veces al mes
    frecuencia = np.random.uniform(1, 10)
    #Insertamos estos valores en a cada uno de los libros
    libros.append([peso, frecuencia])
# Creamos un array con los datos de los libros
data = np.array(libros)
'''
# Normalizamos las características para que tengan una media de cero y una desviación estándar de uno

Esto se hace para evitar que las características con rangos de valores 
muy diferentes tengan más peso en la clasificación que otras características.
'''
X = (data - data.mean(axis=0)) / data.std(axis=0)
# Definimos la arquitectura de la red neuronal perceptrón(creamos la clase perceptron)
class Perceptron:
    #generamos el contructor de la clase perceptron 
    def __init__(self, input_size, output_size):
        #Numero de entradas y salidas de la red neuronal
        self.input_size = input_size
        self.output_size = output_size
        #inicializamos los pesos de la red neuronal al azar utilizando la función np.random.rand().
        self.weights = np.random.rand(input_size, output_size)

    #método que utiliza los pesos de la red neuronal para predecir la clase a la que pertenece cada ejemplo de entrada X.
    #X es una matriz de (m, n), donde m es el número de ejemplos de entrada y n es el número de características de cada ejemplo
    def predict(self, X):
        #devuelve un vector de tamaño (m,) que contiene las etiquetas predichas para cada ejemplo.
        return np.argmax(X @ self.weights, axis=1)
    
    #método que entrena la red neuronal ajustando los pesos de la red mediante el algoritmo del perceptrón.
    #X y y son las matrices de entrada y salida esperada (respectivamente).
    #epochs es el número de iteraciones que el algoritmo de entrenamiento debe ejecutar para ajustar los pesos de la red neuronal
    # y el argumento lr es la tasa de aprendizaje.
    def train(self, X, y, epochs, lr):
        # itera a través de todas las épocas de entrenamiento
        for epoch in range(epochs):
            #calcula la salida de la red utilizando la matriz de entrada X y los pesos actuales de la red
            output = X @ self.weights
            #calcula el error entre la salida esperada y y la salida de la red
            error = y - output
            #ajusta los pesos de la red utilizando el gradiente descendente
            self.weights += lr * X.T @ error
# Creamos una instancia de la red neuronal perceptrón y entrenarla con los datos
perceptron = Perceptron(input_size=2, output_size=4)

#creamos la matriz y, que es la salida esperada para cada entrada X (representa la categoría a la que pertenece el libro)
y = np.zeros((num_libros, 4))
#recorre cada fila de la matriz data
for i, row in enumerate(data):
    #se comprueba el peso y la frecuencia de retiro de cada libro.
    #ligero y poco usado
    if row[0] <= 2 and row[1] <= 5:
        y[i][0] = 1
    #ligero y muy usado
    elif row[0] <= 2 and row[1] >= 5:
        y[i][1] = 1
    #pesado y poco usado
    elif row[0] > 2 and row[1] <= 5:
        y[i][2] = 1
    #pesado y muy usado
    else:
        y[i][3] = 1

#Llamamos al metodo train con la entrada y la salida esperada
#el algoritmo del perceptrón se ejecutará 100 veces. 
#la tasa de aprendizaje establecerá en 0.01.
perceptron.train(X, y, epochs=100, lr=0.01)

# Usamos la red neuronal para clasificar los libros según su peso y frecuencia de uso
conjuntos = perceptron.predict(X)

# Asignar cada conjunto a los libros según su peso y frecuencia de uso
conjuntos_nombre = {0: "Ligeros y poco usados", 1: "Ligeros y muy usados", 2: "Pesados y poco usados", 3: "Pesados y muy usados"}
for i, conjunto in enumerate(conjuntos):
    print(f"El libro {i+1} con peso {data[i][0]:.2f} y frecuencia {data[i][1]:.2f} pertenece al conjunto '{conjuntos_nombre[conjunto]}'.")

# Graficar los resultados y las fronteras de decisión
#Creamos una figura de 8x6
plt.figure(figsize=(8, 6))
#definimos los límites del gráfico utilizando los valores mínimo y máximo de las columnas 0 y 1 de la matriz X
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

#creamos una malla de puntos que cubren todo el espacio definido por los límites
xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.1),
                     np.arange(y_min, y_max, 0.1))

#almacenanamos en la variable Z la clase de cada punto en la malla (0, 1, 2, 3). 
Z = perceptron.predict(np.c_[xx.ravel(), yy.ravel()])

# damos forma a Z para que tenga la misma forma que xx
Z = Z.reshape(xx.shape)

# Graficamos las fronteras de decisión y los puntos de los libros
#definimos el grid donde se graficará Z.
plt.contourf(xx, yy, Z, alpha=0.4)

#graficamos los puntos de los libros con las coordenas en X y Y de los libros
#y le asignamos un color distinto a cada conjunto al que pertenece el libro
plt.scatter(X[:, 0], X[:, 1], c=conjuntos)

#graficamos puntos vacíos de cada color 
for i in range(4):
    #usamos la función plt.scatter, le pasamos como argumentos coordenadas vacías para X e Y, 
    # y se le asigna un color según el índice i del bucle
    #usamos C{}'.format(i) para que el color se corresponda con los colores asignados a los conjuntos de los libros
    plt.scatter([], [], c='C{}'.format(i), label=conjuntos_nombre[i])
#mostrar la leyenda en la figura
plt.legend()
#mostrar la figura completa.
plt.show()
