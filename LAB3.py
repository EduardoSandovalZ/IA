import math
class Node:
   def __init__(self, x, y, g, h, parent):
       self.x = x
       self.y = y
       self.g = g
       self.h = h
       self.parent = parent
   def __lt__(self, other):
       return self.g + self.h < other.g + other.h
   def __eq__(self, other):
       return self.x == other.x and self.y == other.y
def manhattan_distance(x1, y1, x2, y2):
   return abs(x1 - x2) + abs(y1 - y2)
def A_star(board, start, end):
   start_node = Node(start[0], start[1], 0, manhattan_distance(start[0], start[1], end[0], end[1]), None)
   end_node = Node(end[0], end[1], 0, 0, None)  
   open_list = [start_node]
   closed_list = []
   while len(open_list) > 0:
       current_node = min(open_list, key=lambda x: x.g + x.h)
       open_list.remove(current_node)
       closed_list.append(current_node)
       if current_node == end_node:
           path = []
           node = current_node
           while node is not None:
               path.append((node.x, node.y))
               node = node.parent
           return path[::-1]
       neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
       for dx, dy in neighbors:
           x = current_node.x + dx
           y = current_node.y + dy
           if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
               continue
           if board[x][y] == "X":
               continue            
           new_g = current_node.g + manhattan_distance(current_node.x, current_node.y, x, y)
           new_node = Node(x, y, new_g, manhattan_distance(x, y, end_node.x, end_node.y), current_node)
           if any(node == new_node for node in closed_list):
               continue
           if any(node == new_node for node in open_list):
               node = next(node for node in open_list if node == new_node)
               if new_g < node.g:
                   node.g = new_g
                   node.parent = current_node
               continue
           open_list.append(new_node)
   return None
