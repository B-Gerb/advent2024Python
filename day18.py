import heapq

def test(grid):
    start = (0, 0, 0) # steps, x, y
    pq = []
    heapq.heappush(pq, start)
    seen = set()
    while pq:
        value = heapq.heappop(pq)
        if(value[1] == size-1 and value[2] == size-1):
            return True
        if value[1] > 0 and grid[value[2]][value[1]-1] and (value[1]-1, value[2]) not in seen:
            seen.add((value[1]-1, value[2]))
            heapq.heappush(pq, (value[0]+1, value[1]-1, value[2]))


        if value[2] > 0 and grid[value[2]-1][value[1]] and (value[1], value[2]-1) not in seen:
            heapq.heappush(pq, (value[0]+1, value[1], value[2]-1))
            seen.add((value[1], value[2]-1))


        if value[1] < size-1 and grid[value[2]][value[1]+1] and (value[1]+1, value[2]) not in seen:
            heapq.heappush(pq, (value[0]+1, value[1]+1, value[2]))
            seen.add((value[1]+1, value[2]))

        if value[2] < size-1 and grid[value[2]+1][value[1]] and (value[1], value[2]+1) not in seen:
            heapq.heappush(pq, (value[0]+1, value[1], value[2]+1))
            seen.add((value[1], value[2]+1))
    return False
size = 71
maze = [[True for j in range(size)] for i in range(size)]

infoF  = open("day18Info.txt", "r")
infoF = infoF.readlines()
for line in infoF:
    line = line.strip()
    parts = line.split(",")
    X = int(parts[0])
    Y = int(parts[1])
    maze[Y][X] = False
    if not test(maze):
        print(line)
        break

maze = [[True for j in range(size)] for i in range(size)]
bites = 0
right = len(infoF)
left = 0
while(left < right-1):
    copy = []
    for i in maze:
        copy.append(i.copy())
    mid = (left+right)//2
    bites = 0
    for line in infoF:
        if(bites == mid):
            break
        bites += 1
        line = line.strip()
        parts = line.split(",")
        X = int(parts[0])
        Y = int(parts[1])
        copy[Y][X] = False
    if(test(copy)):
        left = mid
    else:
        right = mid
print(infoF[right-1])




