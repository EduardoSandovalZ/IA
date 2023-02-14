# Crea un objeto que representa la figura de la reina
queen = "\u2655"

#Function to verify if the position is available
def is_available(board, row, column, n):
    # Verifying if there's a queen in the same column
    for i in range(row):
        if board[i][column] == queen:
            return False 
    # Verifying if there's a queen in the upper left diagonal
    i, j = row, column
    while i >= 0 and j >= 0:
        if board[i][j] == queen:
            return False
        i -= 1
        j -= 1
    # Verifying if there's a queen in the upper right diagonal
    i, j = row, column
    while i >= 0 and j < n:
        if board[i][j] == queen:
            return False
        i -= 1
        j += 1
    return True

# Using DFS recursive function to place queens
def place_queens(board, row, n):
    if row == n:
        return True
    for column in range(n):
        if is_available(board, row, column, n):
            board[row][column] = queen
            # Moving to the next queen
            if place_queens(board, row + 1, n):
                return True
            # If the current position doesn't lead to a solution, go back to the previous position and try the next column
            board[row][column] = 0
    return False

#Function to print the chessboard
def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()

#Function to solve the n-queens problem
def solve_n_queens(n):
    # Creating the chessboard of size n x n
    board = [[0] * n for _ in range(n)]
    # Placing the queens
    if place_queens(board, 0, n) == False:
        print("No solution exists")
        return False
    # Printing the chessboard
    print_board(board, n)

# Function call with input parameter
solve_n_queens(4)
