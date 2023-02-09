from collections import deque
# A class to represent a graph object
class Graph:
   # Constructor
   def __init__(self, edges, n):
        # lista de listas para representar una lista de adyacencia
       self.adjList = [[] for _ in range(n)]
       # agregar los bordes al grafo no dirigido 
       for (src, dest) in edges:
        #Verificamos que el Tipo de dato de entrada sea una cadena
           if type(src) == str:
                #Si lo son  primero se convierten en enteros
                #Despues agregamos los vértices fuente y destino a la lista de adyacencia correspondiente
               self.adjList[ord(src)].append(ord(dest))
               self.adjList[ord(dest)].append(ord(src))
           else:
                #Si son enteros no les hacemos ninguna conversion
                #Solo agregamos los vértices fuente y destino a la lista de adyacencia correspondiente
               self.adjList[src].append(dest)
               self.adjList[dest].append(src)
#Esta función realiza una búsqueda en profundidad en un grafo, comenzando desde un vértice dado
#La función recibe como argumentos el grafo, el vértice de origen, una lista de descubiertos y el tipo de nodo (cadena o entero)
def iterativeDFS(graph, v, discovered, nodeType):
    #Si el tipo de nodo es una cadena, primero se convierte en un entero
   if nodeType == str:
       v = ord(v)
   # creamos una pila para hacer el BFS
   stack = deque()
   # agregamos el vértice de origen a la pila
   stack.append(v)
   # mientras la pila no esté vacía iteramos sobre cada borde (v, u) del vértice actual
   while stack:
       # Se saca el ultimo vértice de la pila
       v = stack.pop()
       # y verificamos si ya fue descubierto
       if discovered[v]:
            #Si ya ha sido descubierto, se salta a la siguiente iteración del bucle.
           continue
       # si no ha sido descubierto, se marca como descubierto.
       discovered[v] = True
       ##Verificamos Si el tipo de nodo es una cadena, 
       # si lo es se convierte a un valor entero usando "ord"
       if nodeType == str:
            #Y se imprime el carácter
           print(chr(v), end=' ')
       else:
            #Si no, simplemente se imprime el número entero
           print(v, end=' ')


       #almacenamos la lista de vecinos del vértice actual (v)
       adjList = graph.adjList[v]
       # se itera sobre todos los vértices vecinos (u) del vértice actual (v) que aún no han sido descubiertos.
       #iteramos sobre los vecinos de "v" en orden inverso
       for i in reversed(range(len(adjList))):
            #almacenamos el ultimo vecino en u
           u = adjList[i]
           # verificamos si todavía no ha sido descubierto
           if not discovered[u]:
                #Si todavía no ha sido descubierto, se agrega a la pila
               stack.append(u)
if __name__ == '__main__':
   # List of graph edges as per the above diagram
   edges = [
        #RECORRIDOS
        #1ERO 
        #(62,35),(62,80),(35,22),(35,50),(80,65),(80,90)
        #2DO
        #66,44),(66,85),(44,22),(44,50),(85,73),(85,90),(22,9),(22,37),(50,47),(90,88),(90,94),(37,39)
        #3ERO
        #"A","B"),("A","M"),("B","C"),("B","D"),("C","E"),("C","F"),
        #("F","I"),("D","G"),("D","H"),("H","J"),("J","K"),("K","L"),
        #("M","N"),("M","O"),("N","P"),("O","Q")
        #4TO
        #("A","E"),("A","I"),("E","O"),("E","U"),("I","B"),("I","C"),("O","P"),("O","J"),("U","F"),("U","G"),("B","H"),("B","K")
        #5TO
        #(9,4),(9,85),(4,7),(85,40),(85,90),(7,6),(40,22),(40,47),(90,88),(90,94),(22,11),(22,37),(37,39)  
   ]
   # Debe ser mayor a 122, dado que la equivalencia de 'z' en ascii es 122
   n = 122
   # build a graph from the given edges
   graph = Graph(edges, n)
   # to keep track of whether a vertex is discovered or not
   discovered = [False] * n
   # Do iterative DFS traversal from all undiscovered nodes to
   # cover all connected components of a graph
   nodeType = type(edges[0][0]) #Tipo de nodo, String o Integer
   #Orden de parametros (grafo, nodo inicial, arr de descubiertos, tipo de nodo)
   iterativeDFS(graph, edges[0][0], discovered,nodeType)