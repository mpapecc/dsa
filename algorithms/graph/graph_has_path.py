from graph import graph_adjacency_list

def graph_has_path_dfs(graph : dict[str, list[str]], source : str, target : str):
    stack = [source] 
    result = [];
    while stack:
        current = stack.pop();
        if(current == target):
            return True
        result.append(current)
        neighbours = graph[current]

        for item in neighbours:
            stack.append(item)

    return False

def graph_has_path_recursion(graph : dict[str, list[str]], source : str, target : str):
    if(source == target):
        return True

    for item in graph[source]:
        return graph_has_path_recursion(graph, item, target)

    return False

print(graph_has_path_recursion(graph_adjacency_list, "c", "f"))