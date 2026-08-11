graph_adjacency_list = {
    "2" : ["3", "4"],
    "0" : ["8", "1", "5"],
    "1" : ["0"],
    "5" : ["0", "8"],
    "8" : ["0", "5"],
    "3" : ["2", "4"],
    "4" : ["3", "2"]
}

def graph_largest_component(graph : dict[str, list[str]]):  
    visited = set()
    max_count = float("-inf")

    for node in graph_adjacency_list:
        if node not in visited:
            max_count = max(explore(graph, node, visited),max_count) 

    return max_count

def explore(graph : dict[str, list[str]], source : str, visited : set):
    if source in visited:
        return 0
    
    visited.add(source)
    count = 1

    for neighbour in graph[source]:
        count +=1
        explore(graph, neighbour, visited)

    return count
    

print(graph_largest_component(graph_adjacency_list))