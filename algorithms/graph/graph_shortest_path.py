from utils import edges_to_adjacency_list

edges = [
    ["w", "x"],
    ["x", "y"],
    ["z", "y"],
    ["z", "f"],
    ["w", "v"],
    ["v", "k"],
    ["k", "f"]
]

def graph_shortest_path(graph : dict[str, list[str]], source: str, target: str):  

    queue : list[tuple[str, int]]= [(source, 0)]

    while queue:
        (value, distance) = queue.pop(0)

        if value == target:
            return distance

        for neighbour in graph[value]:
            queue.append((neighbour, distance + 1))

    return None



print(graph_shortest_path(edges_to_adjacency_list(edges), "w", "z"))