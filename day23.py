infoF = open("day23Info.txt", "r")
infoF = infoF.readlines()
connections = {}
for line in infoF:
    line = line.strip().split("-")
    if line[0] not in connections:
        connections[line[0]] = set()
    if line[1] not in connections:
        connections[line[1]] = set()
    connections[line[0]].add(line[1])
    connections[line[1]].add(line[0])
values = set()
total = 0
for key in connections: #base layer
    for i in connections[key]: # first connection
        for j in connections[i]: # second
            if key in connections[j]:
                parts = [key, i, j]
                parts.sort()
                values.add(tuple(parts))
total = sum(1 for i in values if any(j[0] == 't' for j in i))
print(total)

longestSet = set()
def process(key, path):
    for i in connections[key]:
        if path <= connections[i]:
            path.add(i)
            process(i, path)
for key in connections:
    #do something here

    for i in connections[key]:
        connectionsSet = set()
        connectionsSet.add(key)
        connectionsSet.add(i)
        process(i, connectionsSet)
        if len(connectionsSet) > len(longestSet):
            longestSet = connectionsSet

print(sorted(longestSet))
print(','.join(sorted(longestSet)))

        
        



