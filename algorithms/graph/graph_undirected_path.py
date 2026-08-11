from utils import edges_to_adjacency_list
from graph import graph_adjacency_list

edges = [
    ["i", "j"],
    ["k", "i"],
    ["m", "k"],
    ["k", "l"],
    ["o", "n"]
]

def graph_undirected_path(graph : dict[str, list[str]], source : str, target : str):
    stack = [source] 
    visited = set()
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current);

            if(current == target):
                return True

            neighbours = graph[current]

            for item in neighbours:
                stack.append(item)

    return False


print(graph_undirected_path(edges_to_adjacency_list(edges), "l", "m"))
