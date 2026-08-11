from graph import graph_adjacency_list

def graph_bfs(graph : dict[str, list[str]], source : str):
    queue = [source] 
    result = [];
    while queue:
        current = queue.pop(0);
        result.append(current)
        neighbours = graph[current]

        for item in neighbours:
            queue.append(item)

    return result

print(graph_bfs(graph_adjacency_list, "a"))