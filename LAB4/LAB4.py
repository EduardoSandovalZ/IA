# Crea un objeto que representa la figura de la reina
REINA = "\u2655"

# Comprueba si la columna está disponible
def columna_disponible(tablero, fila, columna, n):
    for i in range(fila):
        if tablero[i][columna] == REINA:
            return False

    # Comprueba si la diagonal superior izquierda está disponible
    i, j = fila, columna
    while i >= 0 and j >= 0:
        if tablero[i][j] == REINA:
            return False
        i -= 1
        j -= 1

    # Comprueba si la diagonal superior derecha está disponible
    i, j = fila, columna
    while i >= 0 and j < n:
        if tablero[i][j] == REINA:
            return False
        i -= 1
        j += 1

    return True

# Encuentra una solución mediante una búsqueda en profundidad (DFS)
def encontrar_solucion(tablero, fila, n):
    if fila == n:
        return True

    for columna in range(n):
        if columna_disponible(tablero, fila, columna, n):
            tablero[fila][columna] = REINA

            if encontrar_solucion(tablero, fila + 1, n):
                return True

            tablero[fila][columna] = 0

    return False

# Imprime el tablero
def imprimir_tablero(tablero, n):
    for i in range(n):
        for j in range(n):
            print(tablero[i][j], end=" ")
        print()

# Encuentra la solución al problema de las N reinas
def n_reinas(n):
    tablero = [[0] * n for _ in range(n)]
    if encontrar_solucion(tablero, 0, n) == False:
        print("No existe solución")
        return False
    imprimir_tablero(tablero, n)

# Parámetros de entrada
n_reinas(4)
