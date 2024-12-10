


infoF = open('day10Info.txt', 'r')
memorization = {}
zeroValues = []
lines = []
infoF = infoF.readlines()
def search(i,j):
    total = 0
    cur = lines[i][j]
    if (i,j) in memorization:
        return memorization.get((i,j))
    if cur == 9:
        memorization[(i,j)] = 1
        return 1
    else:
        if i > 0 and lines[i-1][j] == cur+1:
            total += search(i-1,j)
        if len(lines)-1 > i  and lines[i+1][j] == cur+1:
            total += search(i+1,j)
        if j>0 and lines[i][j-1] == cur+1:
            total += search(i,j-1)
        if j<len(lines[0])-1 and lines[i][j+1] == cur+1:
            total += search(i,j+1)
        memorization[(i,j)] = total
        return total

for i in range(len(infoF)):
    toAdd = []
    for j in range(len(infoF[i])):
        if infoF[i][j] == '\n':
            break
        if infoF[i][j] == '0':
            zeroValues.append((i,j))
        if infoF[i][j] == '.':
            toAdd.append(-1)
        else:
            toAdd.append(int(infoF[i][j]))
    lines.append(toAdd)
values = 0
for v in zeroValues:
    values += search(v[0], v[1])
print(values)





infoF = open('day10Info.txt', 'r')
memorization = {}
zeroValues = []
lines = []
infoF = infoF.readlines()
def search(i,j):
    total = set()
    cur = lines[i][j]
    if (i,j) in memorization:
        return memorization.get((i,j))
    if cur == 9:
        memorization[(i,j)] = set([(i,j)])
        return memorization.get((i,j))  
    else:
        if i > 0 and lines[i-1][j] == cur+1:
            total.update(search(i-1,j))
        if len(lines)-1 > i  and lines[i+1][j] == cur+1:
            total.update(search(i+1,j))
        if j>0 and lines[i][j-1] == cur+1:
            total.update(search(i,j-1))
        if j<len(lines[0])-1 and lines[i][j+1] == cur+1:
            total.update(search(i,j+1))
        memorization[(i,j)] = total
        return total

for i in range(len(infoF)):
    toAdd = []
    for j in range(len(infoF[i])):
        if infoF[i][j] == '\n':
            break
        if infoF[i][j] == '0':
            zeroValues.append((i,j))
        if infoF[i][j] == '.':
            toAdd.append(-1)
        else:
            toAdd.append(int(infoF[i][j]))
    lines.append(toAdd)
values = 0
for v in zeroValues:
    values += len(search(v[0], v[1]))
print(values)


