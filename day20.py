import heapq
dist = {}
def findPath(start, end, grid):
    queue = []
    heapq.heappush(queue, (0, start, []))
    while queue:
        value = heapq.heappop(queue)
        if value[1] == end:
            for x,pos in enumerate(value[2]):
                dist[pos] = len(value[2])-x
                dist[end] = 0   
            return value[0]
        value[2].append(value[1])
        x, y = value[1]
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] != "#" and (x + dx, y + dy) not in value[2]:
                heapq.heappush(queue, (value[0] + 1, (x + dx, y + dy), value[2].copy()))

def cheating(start, end, grid, limit):
    total = 0
    totalDistance = dist[start]
    for val in dist:

        tried = set()
        for rad in range(2,21):
            for dr in range(rad+1):
                dc = rad-dr
                for dx, dy in [(dr, dc), (-dr, dc), (dr, -dc), (-dr, -dc)]:
                    x,y = val
                    distance = totalDistance - dist[val]
                    if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) and grid[x + dx][y + dy] != "#" and (x+dx, y+dy) not in tried:
                        tried.add((x+dx, y+dy))
                        if distance + dist[(x+dx, y+dy)] + rad <= limit-100:
                            total += 1
    return total
infoF = open("day20Info.txt", "r")

grid = []
infoF = infoF.readlines()

for x,line  in enumerate(infoF):
    if "S" in line:
        start = (x, line.index("S"))
    if "E" in line:
        end = (x, line.index("E"))
    line = line.strip()
    grid.append(list(line))
seconds = findPath(start, end, grid)
print(cheating(start, end, grid, seconds))


