#importamos deque que es una cola doble (se pueden agregar elementos por el frente o por el final)
from collections import deque
#Creamos el metodo de la jarra
#source es la capacidad inicial de las jarras, 
#capacity es la capacidad máxima de las jarras 
#destiny es la cantidad de agua que queremos que tenga.
def jarra(source, capacity, destiny):
    #Creamos una cola doble que se inicializa con el estado inicial de las jarras
    queue = deque([source])
    #Creamos también un conjunto que almacena los estados de las jarras que ya se han visitado
    visited = set([source])
    #Hacemos un bucle mientras nuestra cola no este vacia
    while queue:
        #extraemos el estado actual de la cola 
        current_state = queue.popleft()
        #y se guarda en la variable current_state.
        print(current_state)
        #Si nuestro estado actual es el final deseado, terminamos el bucle
        if current_state == destiny:
            return True
        # Si no, se itera sobre las jarras para encontrar todos los nuevos estados posibles. 
        #Este bucle  itera sobre cada jarra en el estado actual
        for i in range(len(current_state)):
            #Este bucle itera sobre todas las demás jarras
            for j in range(len(current_state)):
                #Para cada jarra, se compara con todas las demás jarras y se considera el caso en que se vacía una jarra en otra.
                #Esta condicion se utiliza para asegurarse de que una jarra no se vacíe en sí misma.
                if i != j:
                    #Asignamos al nuevo estado el estado actual 
                    new_state = list(current_state)
                    #Calculamos la diferencia entre la capacidad de la jarra destino y su cantidad actual de líquido
                    dif = capacity[j] - current_state[j]
                    #Si esta diferencia es mayor o igual que la cantidad de líquido en la jarra de origen, 
                    #podemos vaciar todo el líquido de la jarra de origen a la jarra destino
                    if dif >= current_state[i]:
                        # se actualiza a la suma de la cantidad de líquido en la jarra destino y la jarra de origen 
                        new_state[j] += current_state[i]
                        #se pone a cero la cantidad de líquido en la jarra de origen
                        new_state[i] = 0
                    else:
                        #Si la diferencia es menor que la cantidad de líquido en la jarra de origen, entonces no se puede vaciar todo el líquido a la jarra destino
                        #Se actualiza a la capacidad máxima de la jarra destino.
                        new_state[j] = capacity[j]
                        #Se resta la diferencia a la cantidad de líquido en la jarra de origen.
                        new_state[i] -= dif
                    #Convertimos el nuevo estado a una tupla
                    new_state = tuple(new_state)
                    #Verificamos si aún no se ha visitado previamente
                    #Con esto garantizamos que cada estado se explore una sola vez, evitando ciclos infinitos en la búsqueda.
                    if new_state not in visited:
                        #En caso de que no este visitado se agrega a la cola
                        visited.add(new_state)
                        queue.append(new_state)
    #Si no encontramos solucion salimos de bucle while
    return False

source = (0, 0, 8)
capacity = (3, 5, 8)
destiny = (0, 4, 4)
print(jarra(source, capacity, destiny))
