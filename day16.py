import heapq
# to be stored at score, x, y, dirc

infoF = open("day16Info.txt", "r")
lines = []
infoF = infoF.readlines()
for i,line in enumerate(infoF):
    if "E" in line:
        end = (i, line.index("E"))
    if "S" in line:
        start = (i, line.index("S"))

    lines.append(list(line.strip()))
seen = set()
pq = []
heapq.heappush(pq, (0, start[0], start[1], "right"))

while pq:
    value = pq.pop(0)
    seen.add((value[1], value[2], value[3]))
    if value[1] == end[0] and value[2] == end[1]:
        maxV  = (value[0])
        break
    if value[3] == "up":
        if value[1] > 0 and lines[value[1]-1][value[2]] != "#" and (value[1]-1, value[2], "up") not in seen:
            heapq.heappush(pq, (value[0]+1, value[1]-1, value[2], "up"))


        if value[2] > 0 and lines[value[1]][value[2]-1] != "#" and (value[1], value[2]-1, "left") not in seen:
            heapq.heappush(pq, (value[0]+1001, value[1], value[2]-1, "left"))


        if value[2] < len(lines[0])-1 and lines[value[1]][value[2]+1] != "#" and (value[1], value[2]+1, "right") not in seen:
            heapq.heappush(pq, (value[0]+1001, value[1], value[2]+1, "right"))



    if value[3] == "down":
        if value[1] < len(lines)-1 and lines[value[1]+1][value[2]] != "#" and (value[1]+1, value[2], "down") not in seen:
            heapq.heappush(pq, (value[0]+1, value[1]+1, value[2], "down"))


        if value[2] > 0 and lines[value[1]][value[2]-1] != "#" and (value[1], value[2]-1, "left") not in seen:
            heapq.heappush(pq, (value[0]+1001, value[1], value[2]-1, "left"))


        if value[2] < len(lines[0])-1 and lines[value[1]][value[2]+1] != "#" and (value[1], value[2]+1, "right") not in seen:
            heapq.heappush(pq, (value[0]+1001, value[1], value[2]+1, "right")) 

    if value[3] == "left":
        if value[2] > 0 and lines[value[1]][value[2]-1] != "#" and (value[1], value[2]-1, "left") not in seen:
            heapq.heappush(pq, (value[0]+1, value[1], value[2]-1, "left"))


        if value[1] > 0 and lines[value[1]-1][value[2]] != "#" and (value[1]-1, value[2], "up") not in seen:
            heapq.heappush(pq, (value[0]+1001, value[1]-1, value[2], "up"))


        if value[1] < len(lines)-1 and lines[value[1]+1][value[2]] != "#" and (value[1]+1, value[2], "down") not in seen:
            heapq.heappush(pq, (value[0]+1001, value[1]+1, value[2], "down"))


    if value[3] == "right":
        if value[2] < len(lines[0])-1 and lines[value[1]][value[2]+1] != "#" and (value[1], value[2]+1, "right") not in seen:
            heapq.heappush(pq, (value[0]+1, value[1], value[2]+1, "right"))


        if value[1] > 0 and lines[value[1]-1][value[2]] != "#" and (value[1]-1, value[2], "up") not in seen:
            heapq.heappush(pq, (value[0]+1001, value[1]-1, value[2], "up"))


        if value[1] < len(lines)-1 and lines[value[1]+1][value[2]] != "#" and (value[1]+1, value[2], "down") not in seen:
            heapq.heappush(pq, (value[0]+1001, value[1]+1, value[2], "down"))
print(maxV)

pq = []
bestSpots = set()
heapq.heappush(pq, (0, start[0], start[1], "right", [(start[0], start[1])]))
lowestCost = {}
while pq:
    value = heapq.heappop(pq)

    if (value[1], value[2], value[3]) in lowestCost and lowestCost[(value[1], value[2], value[3])] != value[0]:
        continue
    else:
        lowestCost[(value[1], value[2], value[3])] = value[0]
    if value[0] > maxV:
        break
    if value[1] == end[0] and value[2] == end[1]:
        if value[0] == maxV:
            bestSpots.update(value[4])
    if value[3] == "up":
        if value[1] > 0 and lines[value[1]-1][value[2]] != "#" and (value[1]-1, value[2]) not in value[4]:
            heapq.heappush(pq, (value[0]+1, value[1]-1, value[2], "up", value[4] + [(value[1]-1, value[2])]))


        if value[2] > 0 and lines[value[1]][value[2]-1] != "#" and (value[1], value[2]-1) not in value[4]:
            heapq.heappush(pq, (value[0]+1001, value[1], value[2]-1, "left", value[4] + [(value[1], value[2]-1)]))


        if value[2] < len(lines[0])-1 and lines[value[1]][value[2]+1] != "#" and (value[1], value[2]+1) not in value[4]:
            heapq.heappush(pq, (value[0]+1001, value[1], value[2]+1, "right", value[4] + [(value[1], value[2]+1)]))



    if value[3] == "down":
        if value[1] < len(lines)-1 and lines[value[1]+1][value[2]] != "#" and (value[1]+1, value[2]) not in value[4]:
            heapq.heappush(pq, (value[0]+1, value[1]+1, value[2], "down", value[4] + [(value[1]+1, value[2])]))


        if value[2] > 0 and lines[value[1]][value[2]-1] != "#" and (value[1], value[2]-1) not in value[4]:
            heapq.heappush(pq, (value[0]+1001, value[1], value[2]-1, "left", value[4] + [(value[1], value[2]-1)]))


        if value[2] < len(lines[0])-1 and lines[value[1]][value[2]+1] != "#" and (value[1], value[2]+1) not in value[4]:
            heapq.heappush(pq, (value[0]+1001, value[1], value[2]+1, "right", value[4] + [(value[1], value[2]+1)])) 

    if value[3] == "left":
        if value[2] > 0 and lines[value[1]][value[2]-1] != "#" and (value[1], value[2]-1) not in value[4]:
            heapq.heappush(pq, (value[0]+1, value[1], value[2]-1, "left", value[4] + [(value[1], value[2]-1)]))


        if value[1] > 0 and lines[value[1]-1][value[2]] != "#" and (value[1]-1, value[2]) not in value[4]:
            heapq.heappush(pq, (value[0]+1001, value[1]-1, value[2], "up", value[4] + [(value[1]-1, value[2])]))


        if value[1] < len(lines)-1 and lines[value[1]+1][value[2]] != "#" and (value[1]+1, value[2]) not in value[4]:
            heapq.heappush(pq, (value[0]+1001, value[1]+1, value[2], "down", value[4] + [(value[1]+1, value[2])]))


    if value[3] == "right":
        if value[2] < len(lines[0])-1 and lines[value[1]][value[2]+1] != "#" and (value[1], value[2]+1) not in value[4]:
            heapq.heappush(pq, (value[0]+1, value[1], value[2]+1, "right", value[4] + [(value[1], value[2]+1)]))


        if value[1] > 0 and lines[value[1]-1][value[2]] != "#" and (value[1]-1, value[2]) not in value[4]:
            heapq.heappush(pq, (value[0]+1001, value[1]-1, value[2], "up", value[4] + [(value[1]-1, value[2])]))


        if value[1] < len(lines)-1 and lines[value[1]+1][value[2]] != "#" and (value[1]+1, value[2]) not in value[4]:
            heapq.heappush(pq, (value[0]+1001, value[1]+1, value[2], "down", value[4] + [(value[1]+1, value[2])]))   
print(len(bestSpots))