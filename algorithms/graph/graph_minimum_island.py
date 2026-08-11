grid = [
    ["W", "L", "W", "W", "L", "W"],
    ["L", "L", "W", "W", "L", "W"],
    ["W", "L", "W", "W", "W", "W"],
    ["W", "W", "W", "L", "L", "W"],
    ["W", "W", "W", "L", "L", "W"],
    ["W", "W", "W", "L", "W", "W"]
]

def graph_minimum_island(grid : list[list[str]]):  
    visited = set()
    min_count = float("inf")

    for y, row in enumerate(grid):
        for x, column in enumerate(row):
            if column == "L" and (x,y) not in visited:
                min_count = min( explore(grid, (x,y), visited), min_count)

    return min_count

def explore(grid : list[list[str]], point : tuple[int,int], visited: set):
    [x, y] = point
    
    if x < 0 or x > len(grid[0]) - 1 or y < 0 or y  > len(grid) -1:
        return 0
    
    if grid[y][x] == "W":
        return 0
    
    if point in visited:
        return 0

    count = 1
    
    visited.add(point)

    count += explore(grid, (x + 1, y), visited)
    count += explore(grid, (x - 1, y), visited)
    count += explore(grid, (x, y + 1), visited)
    count += explore(grid, (x, y - 1), visited)

    return count;
    

print(graph_minimum_island(grid))