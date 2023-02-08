from collections import deque

def jarra(source, capacity, destiny):

    queue = deque([source])
    visited = set([source])

    while queue:
        current_state = queue.popleft()
        print(current_state)
        if current_state == destiny:
            return True
        for i in range(len(current_state)):
            for j in range(len(current_state)):
                if i != j:
                    new_state = list(current_state)
                    dif = capacity[j] - current_state[j]

                    if dif >= current_state[i]:

                        new_state[j] += current_state[i]
                        new_state[i] = 0

                    else:
                        new_state[j] = capacity[j]
                        new_state[i] -= dif

                    new_state = tuple(new_state)

                    if new_state not in visited:

                        visited.add(new_state)
                        queue.append(new_state)

    return False

source = (0, 0, 8)
capacity = (3, 5, 8)
destiny = (0, 4, 4)
print(jarra(source, capacity, destiny))
