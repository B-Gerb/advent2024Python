infoF = open('day9Info.txt', 'r')
newString = []
val = infoF.readline()
digit = 0
for i in range(len(val)):
    if i%2 == 0:
        toExtend = [str(digit)] * int(val[i:i+1])
        digit +=1
    else:
        toExtend = ["."] *int(val[i:i+1])
    newString.extend(toExtend)
for i in range(len(newString)-1, 0, -1):
    if newString[i] != ".":
        index = newString.index(".")
        if index > i:
            break
        newString[index] = newString[i]
        newString[i] = "."
total = 0
for i in range(len(newString)):
    if newString[i] == ".":
        break
    total += (i*int(newString[i]))
print(total)
infoF.close



infoF = open('day9Info.txt', 'r')
newString = []
val = infoF.readline()
digit = 0
for i in range(len(val)):
    if i%2 == 0:
        toAppend = i/2
    else:
        toAppend = -1
    newString.append((int(val[i:i+1]), int(toAppend)))
i = len(newString)-1
alreadyProcessed = set()
while i>0:
    if newString[i][1] != -1 and newString[i][1] not in alreadyProcessed:
        alreadyProcessed.add(newString[i][1])
        needed = newString[i][0]

        for v in range(i):
            if newString[v][1] == -1 and newString[v][0] >= needed:
                removed = newString[v]
                
                newString.insert(v, newString[i])
                del newString[v+1]

                newString[i] = (newString[i][0], -1)

                if(removed[0] - needed >0):
                    newString.insert(v+1, (removed[0] - needed, -1))
                    i+=1
                break
        
    i-= 1


for i in range(len(newString)):
    if newString[i][1] != -1:
        total += sum(range(index, index+newString[i][0]))*newString[i][1]
    index += newString[i][0]
print(total)
infoF.close