valuesnum = {
    "7": (0, 0), "8": (0, 1), "9": (0, 2),
    "4": (1, 0), "5": (1, 1), "6": (1, 2),
    "1": (2, 0), "2": (2, 1), "3": (2, 2),
    "0": (3, 1), "A": (3, 2),
    (0, 0): "7", (0, 1): "8", (0, 2): "9",
    (1, 0): "4", (1, 1): "5", (1, 2): "6",
    (2, 0): "1", (2, 1): "2", (2, 2): "3",
    (3, 1): "0", (3, 2): "A"
}

valuesDir = {
    (0, 1): "^", (0, 2): "A", (1, 0): "<",
    (1, 1): "v", (1, 2): ">", 
    "^": (0, 1), "A": (0, 2), "<": (1, 0),
    "v": (1, 1), ">": (1, 2)
}
infoF = open("day21Info.txt", "r")    
import heapq
from functools import cache        
def numToDir(num):
    full = [""]
    cur = "A"
    while num:
        prev = cur
        cur = num[0:1]
        num = num[1:]
        newR, newC = valuesnum[cur]
        queue = []
        heapq.heappush(queue, (0, "", valuesnum[prev], set()))
        newFull = []
        found = -1
        while queue:
            value = heapq.heappop(queue)
            value[3].add(value[2])
            if found != -1 and found < len(value[1]):
                break

            if value[2] == (newR, newC):
                found = len(value[1])
                for x in full:
                    newFull.append(x+value[1]+"A") 
                continue           
            if (value[2][0] +1, value[2][1]) in valuesnum and (value[2][0] +1, value[2][1]) not in value[3]:
                heapq.heappush(queue, (value[0]+1, value[1]+"v", (value[2][0] +1, value[2][1]), value[3].copy()))
            if (value[2][0] -1, value[2][1]) in valuesnum and (value[2][0] -1, value[2][1]) not in value[3]:
                heapq.heappush(queue, (value[0]+1, value[1]+"^", (value[2][0] -1, value[2][1]), value[3].copy()))
            if (value[2][0], value[2][1]+1) in valuesnum and (value[2][0], value[2][1]+1) not in value[3]:
                heapq.heappush(queue, (value[0]+1, value[1]+">", (value[2][0], value[2][1]+1), value[3].copy()))
            if (value[2][0], value[2][1]-1) in valuesnum and (value[2][0], value[2][1]-1) not in value[3]:
                heapq.heappush(queue, (value[0]+1, value[1]+"<", (value[2][0], value[2][1]-1), value[3].copy()))
        full = newFull
    return full

def computePath(prev, cur):
    allPaths = []
    queue = []
    heapq.heappush(queue, (0, "", valuesDir[prev], set()))
    new_pos = valuesDir[cur]
    old_pos = valuesDir[prev]
    found = -1
    while queue:
        value = heapq.heappop(queue)
        value[3].add(value[2])
        if found != -1 and found < len(value[1]):
            break
        if value[2] == new_pos:
            found = len(value[1])
            
            allPaths.append(value[1] + "A")
            continue
        if (value[2][0] +1, value[2][1]) in valuesDir and (value[2][0] +1, value[2][1]) not in value[3]:
            heapq.heappush(queue, (value[0]+1, value[1]+"v", (value[2][0] +1, value[2][1]), value[3].copy()))
        if (value[2][0] -1, value[2][1]) in valuesDir and (value[2][0] -1, value[2][1]) not in value[3]:
            heapq.heappush(queue, (value[0]+1, value[1]+"^", (value[2][0] -1, value[2][1]), value[3].copy()))
        if (value[2][0], value[2][1]+1) in valuesDir and (value[2][0], value[2][1]+1) not in value[3]:
            heapq.heappush(queue, (value[0]+1, value[1]+">", (value[2][0], value[2][1]+1), value[3].copy()))
        if (value[2][0], value[2][1]-1) in valuesDir and (value[2][0], value[2][1]-1) not in value[3]:
            heapq.heappush(queue, (value[0]+1, value[1]+"<", (value[2][0], value[2][1]-1), value[3].copy()))
            

    return allPaths
@cache
def dirToDir(cur, depth):
    if depth == 0:
        return len(cur)

    directions=[]
    total = 0
    for i in range(len(cur)):
        if i == 0:
            values = computePath("A", cur[i])
            minNum = float("inf")
            for v in values:
                minNum = min(minNum, dirToDir( v, depth-1))
            total += minNum
        else:
            values = computePath(cur[i-1], cur[i])
            minNum = float("inf")
            for v in values:
                minNum = min(minNum, dirToDir( v, depth-1))
            total += minNum    
    return total

total = 0 
amt = 0
for line in infoF:
    line = line.strip()
    number = int(line[:-1])
    start = "A"
    values = numToDir(line)
    newVal = []
    for v in values:
        newVal.append(dirToDir(v, 25))
    
    values = newVal
    values = sorted(values)
    total += number*values[0]
print(total)
