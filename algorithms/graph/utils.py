def edges_to_adjacency_list(edges: list[list[str]]):
    adjacency_list : dict[str, list[str]] = {}

    for edge in edges:
        left = edge[0]
        right = edge[1]

        if(left in adjacency_list):
            adjacency_list[left].append(right)
        else:
            adjacency_list[left] = [right]

        if(right in adjacency_list):
            adjacency_list[right].append(left)
        else:
            adjacency_list[right] = [left]

    return adjacency_list
        

        