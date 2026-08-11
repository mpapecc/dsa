from graph import graph_adjacency_list

def graph_dfs(graph : dict[str, list[str]], source : str):
    stack = [source] 
    result = []
    while stack:
        current = stack.pop()
        result.append(current)
        neighbours = graph[current]

        for item in neighbours:
            stack.append(item)

    return result

def graph_dfs_recursion(graph : dict[str, list[str]], source : str):
    print(source)

    for item in graph_adjacency_list[source]:
        graph_dfs_recursion(graph,item)

print(graph_dfs_recursion(graph_adjacency_list, "a"))