graph_adjacency_list = {
    "3" : [],
    "4" : ["6"],
    "6" : ["4", "5", "7", "8"],
    "8" : ["6"],
    "7" : ["6"],
    "5" : ["6"],
    "1" : ["2"],
    "2" : ["1"]
}

def graph_connected_components_count(graph : dict[str, list[str]]):
    visited = set()
    count = 0

    for node in graph:
        if explore_recursive(graph, node, visited):
            count += 1

    return count

def explore(graph : dict[str, list[str]], source: str, visited : set):
    if source in visited:
        return False

    queue = [source]

    while queue:
        current = queue.pop()
        visited.add(current)

        for item in graph[current]:
            explore(graph, item, visited)

    return True

def explore_recursive(graph : dict[str, list[str]], source: str, visited : set):
    if source in visited:
        return False

    for item in graph[source]:
        explore(graph, item, visited)

    return True



print(graph_connected_components_count(graph_adjacency_list))