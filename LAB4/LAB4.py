'''
Este código resuelve el problema de las N reinas, que consiste en colocar 
N reinas en un tablero de ajedrez de NxN casillas de tal forma que ninguna reina amenace a otra.
'''
#Colocamos el símbolo unicode correspondiente a la figura de la reina del ajedrez
queen = "\u2655"
#función que comprueba si una posición en el tablero está disponible para colocar una reina
def is_available(board, row, column, n):
   #Recorremos todas las filas por encima de la fila actual (hasta la fila 0)
   for i in range(row):
       #comprobamos si hay una reina en la misma columna
       if board[i][column] == queen:
           #Si encuentra una reina, devuelve "False", lo que indica que la posición no está disponible
           return False
    #nicializamos las variables "i" y "j" con las coordenadas de la posición actual en el tablero que se está evaluando
   i, j = row, column
   #recorremos diagonalmente hacia arriba y hacia la izquierda desde la posición actual hasta la fila y columna (0, 0) del tablero.
   while i >= 0 and j >= 0:
       #compruebamos si hay una reina en la posición actual
       if board[i][j] == queen:
           #Si se encuentra una reina, significa que la posición actual no está disponible y se devuelve "False"
           return False
       #Si no se encuentra una reina, se actualizan las variables "i" y "j" para moverse a la siguiente posición en la diagonal.
       i -= 1
       j -= 1
   i, j = row, column
   #realiza una comprobación en diagonal hacia arriba y hacia la derecha 
   # desde la posición actual hasta la fila 0 y la columna "n-1" del tablero
   while i >= 0 and j < n:
       #compruebamos si hay una reina en la posición actual
       if board[i][j] == queen:
           #Si se encuentra una reina, significa que la posición actual no está disponible y se devuelve "False"
           return False
       #Si no se encuentra una reina, se actualizan las variables "i" y "j" para moverse a la siguiente posición en la diagonal.
       i -= 1
       j += 1
   return True
#función recursiva que coloca las reinas en el tablero
def place_queens(board, row, n):
   #comprobamos si se han colocado todas las N reinas
   if row == n:
       #Si es asi, devuelve un true
       return True
   #Si no, itera a través de todas las columnas en la fila actual
   for column in range(n):
       #compruebamos si cada columna está disponible utilizando la función 
       if is_available(board, row, column, n):
           #si la columna está disponible, se coloca la reina en esa posición
           board[row][column] = queen
           #llamamos a la función "place_queens" para colocar la siguiente reina en la siguiente fila
           if place_queens(board, row + 1, n):
               #Si devuelve "True", significa que todas las reinas se han colocado correctamente
               return True
           #Si no se colocan todas las reinas, la función deshace la última jugada colocando un 0 
           #y sigue explorando otras posibles soluciones
           board[row][column] = 0
    #Si no se encuentran soluciones para una fila determinada, se vuelve al nivel anterior de la 
    # recursión para explorar otras posibilidades.
   return False


#función que imprime el tablero con las reinas colocadas. 
def print_board(board, n):
   #itera a través de todas las filas y columnas de la matriz del tablero 
   for i in range(n):
       for j in range(n):
           #Comprueba si hay una reina en esa posición.
           if board[i][j] == queen:
               #Si hay una reina, imprime el símbolo unicode correspondiente a la figura de la reina
               print(f"{board[i][j]}", end=" ")
           else:
               #Si no hay una reina, imprime un cuadrado en blanco 
               print(f"\u25A1", end=" ")
        #Imprimimos una nueva línea después de imprimir todas las columnas de una fila       
       print()
#Funcion para resolver el problema de las N reinas
def solve_n_queens(n):
   #crea un tablero vacío de n x n, utilizando una lista anidada y el operador "*" para generar n copias de la lista [0]
   board = [[0] * n for _ in range(n)]
   #Si no encontramos una solución, devuelve "False" y se imprime un mensaje de error indicando que no se encontró una solución
   if place_queens(board, 0, n) == False:
       print("No solution exists")
       return False
   #Si encuentramos una solución, devuelve "True" y se imprime el tablero solución utilizando la función
   print_board(board, n)

solve_n_queens(8)

