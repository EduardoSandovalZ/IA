import math

class Node:
    #Metodo contructor, teniendo en cuenta posicion (x,y), distancia de inicio a fin (g) y la distancia estimada hasta el nodo final (h)
    #Tambien debemos de tener una referencia al nodo padre (el anterior)
    def __init__(self, x, y, g, h, parent):
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.parent = parent
    #Metodo para comparar los objetos de la clase node, esto para determinar cual tiene un menor costo
    def __lt__(self, other):
        return self.g + self.h < other.g + other.h
    #Metodo para comparar los objetos de la clase node, esto para determinar si sus coordenadas son las mismas  
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

"""
#Metodo que realiza el calculo de la distancia de Manhattan.
def manhattan_distance(x1, y1, x2, y2):
   return abs(x1 - x2) + abs(y1 - y2)
"""
#Metodo que realiza el calculo de la distancia euclidiana.
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
#Metodo A estrella 
def A_star(board, start, end):
   start_node = Node(start[0], start[1], 0, euclidean_distance(start[0], start[1], end[0], end[1]), None)
   end_node = Node(end[0], end[1], 0, 0, None)
   #Creamos 2 listas  
   #open_list contiene solo el nodo de inicio y contiene los nodos que aun no han sido revisados
   open_list = [start_node]
   #Closed_list ya revisados
   closed_list = []
   #Mientras haya nodos por explorar, se realizara este bucle
   while len(open_list) > 0:
        #Se selecciona el nodo con el costo más bajo de la lista open_list, 
        #este costo es igual a g + h. g es el costo hasta el nodo actual y h es la estimación del costo hasta el nodo final.
       current_node = min(open_list, key=lambda x: x.g + x.h)
       #Ya que seleccionamos el nodo actual lo eliminamos de la open list 
       open_list.remove(current_node)
       #y lo pasamos a la closed list
       closed_list.append(current_node)
       #Verificamos que el nodo acttual sea el nodo de destino
       if current_node == end_node:
            #en caso de que sea asi,creamos una lista que contendra el camino 
           path = []
           #asignamos el nodo actual a una nueva variable llamada nodo
           node = current_node
           #y hacemos un bucle para hacer un recorrido desde nuestra posicion actual hasta el inicio
           while node is not None:
                #agregamos al path las cordenadas x,y
               path.append((node.x, node.y))
               #y usamos el nodo padre para ir 
               node = node.parent
           return path[::-1]
        #Generamos la lista de vecinos del nodo actual en base a las 4 direcciones
        #Arriba, abajo, derecha, izquierda
       neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        #Recorremos cada uno de los vecinos 
       for dx, dy in neighbors:
            #le asignamos a x el desplazamiento en x a la cordenada del nodo actual en x
           x = current_node.x + dx
            #le asignamos a y el desplazamiento en y a la cordenada del nodo actual en y
           y = current_node.y + dy
            #Verificamos que estos se encuentren dentro del mapa
           if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
               continue
           #Tambien confirmamos que este nodo vecino no sea un obstaculo
           if board[x][y] == "X":
               continue            
            #Calculamos el costo de g del nuevo nodo, sumando el costo del nodo actual 
            # y la distancia Euclidiana desde el nodo actual hasta el vecino.
           new_g = current_node.g + euclidean_distance(current_node.x, current_node.y, x, y)
            #Creamos un nuevo nodo con las coordenadas, el costo g calculado, una estimación h de la distancia Euclidiana hasta el nodo final 
            #y el nodo actual como su nodo padre.
           new_node = Node(x, y, new_g, euclidean_distance(x, y, end_node.x, end_node.y), current_node)
            #Verificamos si el nuevo nodo se encuentra en la closed_list, si es así, 
            #saltamos a la siguiente iteración sin agregar el nodo a la open_list.
           if any(node == new_node for node in closed_list):
               continue
            #Si el nuevo nodo no está en la closed_list, verificamos si se encuentra en la open_list. 
           if any(node == new_node for node in open_list):
                 #Si es así, se actualiza el costo g y el nodo padre si es necesario.
               node = next(node for node in open_list if node == new_node)
               if new_g < node.g:
                   node.g = new_g
                   node.parent = current_node
               continue
            #Si el nuevo nodo no esta en ninguna de las dos listas, lo agregamos a la open_list.
           open_list.append(new_node)
   return None

'''
board = [['S', 'X', ' ', ' ', ' '],
        [' ', 'X', ' ', 'X', ' '],
        [' ', 'X', ' ', 'X', ' '],
        [' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', 'G', ' '],
        [' ', ' ', ' ', ' ', ' ']]

start = (0, 0)
end = (4, 3)
'''

board = [[' ', ' ', ' ', ' ', ' '],
        [' ', 'S', ' ', ' ', ' '],
        [' ', 'X', 'X', ' ', ' '],
        [' ', ' ', 'X', ' ', ' '],
        [' ', 'X', 'X', 'X', ' '],
        [' ', ' ', ' ', 'G', ' '],
        [' ', ' ', ' ', ' ', ' ']]
start = (1, 1)
end = (5, 3)

path = A_star(board, start, end)
#Verificamos que exista el camino
if path is not None:
    #Recorremos las filas y las columnas del tablero
    for i in range(len(board)):
        for j in range(len(board[0])):
            #Si la fila i y la columna j existen en el camino
            if (i, j) in path:
                #Se imprimen por que dorman parte del camino
                print(8, end=" ")
                #Verificamos que esa fila y esa columna sea una X
            elif board[i][j] == "X":
                #Si lo es, imprimimos un 0
                print(0, end=" ")
            else:
                #Si las condiciones no se cumple, asumimos  que la ubicación actual es un espacio vacio.
                print(1, end=" ")
        print()
else:
    print("No path found")

"""
if path is not None:
    for node in path:
        print(node)
else:
    print("No path found")
"""
