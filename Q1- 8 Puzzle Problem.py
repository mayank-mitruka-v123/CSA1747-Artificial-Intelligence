from collections import deque

# Define the goal state
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Initial state
start_state = (1, 2, 3, 4, 5, 6, 0, 8, 7)

# Initialize BFS components
queue = deque([start_state])
visited = set()
parent = {start_state: None}

# BFS Loop
while queue:
    current = queue.popleft()
    
    # Check if the current state is the goal state
    if current == GOAL_STATE:
        # Reconstruct the path
        path = []
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()  # Reverse the path to get the correct order
        for step in path:
            print(step)
        break

    # Get neighbors
    zero_index = current.index(0)
    zero_x, zero_y = divmod(zero_index, 3)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in moves:
        new_x, new_y = zero_x + dx, zero_y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_zero_index = new_x * 3 + new_y
            new_state = list(current)
            new_state[zero_index], new_state[new_zero_index] = new_state[new_zero_index], new_state[zero_index]
            new_state = tuple(new_state)
            
            if new_state not in visited:
                visited.add(new_state)
                parent[new_state] = current
                queue.append(new_state)
else:
    print("No solution found")
