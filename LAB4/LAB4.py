queen = "\u2655"
def is_available(board, row, column, n):
   for i in range(row):
       if board[i][column] == queen:
           return False
   i, j = row, column
   while i >= 0 and j >= 0:
       if board[i][j] == queen:
           return False
       i -= 1
       j -= 1
   i, j = row, column
   while i >= 0 and j < n:
       if board[i][j] == queen:
           return False
       i -= 1
       j += 1
   return True
def place_queens(board, row, n):
   if row == n:
       return True
   for column in range(n):
       if is_available(board, row, column, n):
           board[row][column] = queen
           if place_queens(board, row + 1, n):
               return True
           board[row][column] = 0
   return False
def print_board(board, n):
   for i in range(n):
       for j in range(n):
           if board[i][j] == queen:
               print(f"{board[i][j]}", end=" ")
           else:
               print(f"\u25A1", end=" ")
       print()
def solve_n_queens(n):
   board = [[0] * n for _ in range(n)]
   if place_queens(board, 0, n) == False:
       print("No solution exists")
       return False
   print_board(board, n)
solve_n_queens(8)

