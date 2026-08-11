grid = [
    ["W", "L", "W", "W", "L", "W"],
    ["L", "L", "W", "W", "L", "W"],
    ["W", "L", "W", "W", "W", "W"],
    ["W", "W", "W", "L", "L", "W"],
    ["W", "L", "W", "L", "L", "W"],
    ["W", "W", "W", "W", "W", "W"]
]

def graph_island_count(grid : list[list[str]]):  
    visited = set()
    count = 0

    for y, row in enumerate(grid):
        for x, _ in enumerate(row):
            if explore(grid, (x,y), visited):
                count +=1

    return count

def explore(grid : list[list[str]], point : tuple[int,int], visited: set):
    [x, y] = point
    
    if x < 0 or x > len(grid[0]) - 1 or y < 0 or y  > len(grid) -1:
        return False
    
    if grid[y][x] == "W":
        return False
    
    if point in visited:
        return False
    
    visited.add(point)

    explore(grid, (x + 1, y), visited)
    explore(grid, (x - 1, y), visited)
    explore(grid, (x, y + 1), visited)
    explore(grid, (x, y - 1), visited)

    return True;
    

print(graph_island_count(grid))