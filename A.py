from queue import PriorityQueue

def a_star(graph, start, goal, h):
    pq = PriorityQueue()
    pq.put((0, start))
    came_from = {start: None}
    g_score = {start: 0}

    while not pq.empty():
        current = pq.get()[1]

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for neighbor, weight in graph[current].items():
            tentative_g = g_score[current] + weight
            if neighbor not in g_score or tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + h[neighbor]
                pq.put((f_score, neighbor))
                came_from[neighbor] = current

    return None

def input_graph():
    graph = {}
    print("Enter the graph:")
    while True:
        line = input("Enter node connections (e.g., A B 1) or 'done' to finish: ")
        if line.lower() == 'done':
            break
        parts = line.split()
        if len(parts) == 3:
            node1, node2, weight = parts
            weight = int(weight)
            if node1 not in graph:
                graph[node1] = {}
            graph[node1][node2] = weight
            if node2 not in graph:
                graph[node2] = {}
    return graph

def input_heuristics():
    heuristics = {}
    print("Enter heuristic values:")
    while True:
        line = input("Enter node and heuristic value (e.g., A 4) or 'done' to finish: ")
        if line.lower() == 'done':
            break
        parts = line.split()
        if len(parts) == 2:
            node, value = parts
            heuristics[node] = int(value)
    return heuristics

def main():
    graph = input_graph()
    h = input_heuristics()
    start = input("Enter the start node: ")
    goal = input("Enter the goal node: ")

    path = a_star(graph, start, goal, h)
    if path:
        print("Shortest path:", path)
    else:
        print("No path found.")

if __name__ == "__main__":
    main()
