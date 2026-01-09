import heapq

def astar(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))
    cost = {start: 0}
    parent = {start: None}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            break

        for neighbor, weight in graph[current]:
            new_cost = cost[current] + weight
            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + heuristic[neighbor]
                heapq.heappush(open_list, (priority, neighbor))
                parent[neighbor] = current

    path = []
    while goal:
        path.append(goal)
        goal = parent[goal]
    path.reverse()
    return path

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1)],
    'C': [('D', 1)],
    'D': []
}

heuristic = {
    'A': 3,
    'B': 2,
    'C': 1,
    'D': 0
}

print("A* Path:", astar(graph, 'A', 'D', heuristic))
