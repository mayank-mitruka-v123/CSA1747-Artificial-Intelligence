import heapq

class PuzzleState:
    def __init__(self, board, goal, moves=0, previous=None):
        self.board = board
        self.goal = goal
        self.moves = moves
        self.previous = previous
        self.priority = self.moves + self.manhattan_distance()

    def manhattan_distance(self):
        """Calculate the Manhattan distance from the current state to the goal state."""
        distance = 0
        for i in range(3):
            for j in range(3):
                value = self.board[i][j]
                if value != 0:
                    goal_i, goal_j = divmod(self.goal.index(value), 3)
                    distance += abs(i - goal_i) + abs(j - goal_j)
        return distance

    def get_neighbors(self):
        """Generate the neighboring states by sliding a tile."""
        neighbors = []
        x, y = next((i, j) for i in range(3) for j in range(3) if self.board[i][j] == 0)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < 3 and 0 <= new_y < 3:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                neighbors.append(PuzzleState(new_board, self.goal, self.moves + 1, self))
        
        return neighbors

    def is_goal(self):
        """Check if the current state is the goal state."""
        return self.board == [self.goal[i:i + 3] for i in range(0, 9, 3)]

    def __lt__(self, other):
        return self.priority < other.priority

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.board))


def solve_puzzle(start, goal):
    """Solve the 8-puzzle problem using the A* algorithm."""
    open_set = []
    closed_set = set()

    start_state = PuzzleState(start, goal)
    heapq.heappush(open_set, start_state)

    while open_set:
        current_state = heapq.heappop(open_set)

        if current_state.is_goal():
            return current_state

        closed_set.add(current_state)

        for neighbor in current_state.get_neighbors():
            if neighbor in closed_set:
                continue

            heapq.heappush(open_set, neighbor)

    return None


def print_solution(solution):
    """Print the solution steps."""
    path = []
    while solution:
        path.append(solution.board)
        solution = solution.previous
    path.reverse()
    
    for step in path:
        for row in step:
            print(row)
        print()


# Example usage
start = [
    [1, 2, 3],
    [4, 0, 6],
    [7, 5, 8]
]

goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]

solution = solve_puzzle(start, goal)

if solution:
    print("Solution found!")
    print_solution(solution)
else:
    print("No solution exists.")
