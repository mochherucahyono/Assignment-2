def gbfs(grid, start, goal):
    from queue import PriorityQueue
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    visited = set()
    pq = PriorityQueue()
    pq.put((0, start, [start]))

    def heuristic(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    while not pq.empty():
        h, current, path = pq.get()
        if current == goal:
            return path

        if current in visited:
            continue

        visited.add(current)
        for dx, dy in directions:
            nx, ny = current[0]+dx, current[1]+dy
            if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny] != 'T':
                neighbor = (nx, ny)
                if neighbor not in visited:
                    pq.put((heuristic(neighbor, goal), neighbor, path + [neighbor]))
    return None

# Contoh grid
city_grid = [
    ['S', '.', '.', 'T', 'H'],
    ['T', 'T', '.', 'T', '.'],
    ['.', '.', '.', '.', '.']
]

start = (0, 0)
goal = (0, 4)
print("GBFS Path from S to H:", gbfs(city_grid, start, goal))

