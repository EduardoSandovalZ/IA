# Unicode representation of the queen symbol
queen = "\u2655"

# Check if the position is available for placing the queen
def is_available(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == queen:
            return False

    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == queen:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == queen:
            return False
        i -= 1
        j += 1

    return True

# Place the queens on the board using depth-first search
def place_queens(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_available(board, row, col, n):
            board[row][col] = queen

            if place_queens(board, row + 1, n):
                return True

            board[row][col] = 0

    return False

# Print the chessboard
def print_board(board, n):
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                print("\u25A1", end=" ")
            else:
                print("\u25A0", end=" ")
        print()
        for j in range(n):
            if board[i][j] == queen:
                print(queen, end=" ")
            else:
                print("\u2001", end=" ")
        print()

# Solve the N-Queens problem
def solve_n_queens(n):
    board = [[0] * n for _ in range(n)]
    if place_queens(board, 0, n) == False:
        print("No solution exists")
        return False
    print_board(board, n)

# Solve the 4-Queens problem
solve_n_queens(4)
