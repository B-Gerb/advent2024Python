infoF = open("day22Info.txt", "r")
infoF = infoF.readlines()
def step(a):
    a = (a^(a*64)) % 16777216
    a = (a^(a//32)) % 16777216
    a = (a^(a*2048)) % 16777216
    return a
    
total = 0
listOfAllValues = {}

for line in infoF:
    valuesUsed = set()
    toAppend = set()
    line = line.strip()
    num = int(line)
    rem = num
    pastFour = []

    previous = num%10
    for i in range(2000):
        
        if len(pastFour) == 4:
            pastFour = pastFour[1:]
        num = step(num)
        pastFour.append(num%10-previous)
        previous = num%10
        if len(pastFour) == 4:
            if (pastFour[0], pastFour[1], pastFour[2], pastFour[3]) in valuesUsed:
                continue
            else:
                if (pastFour[0], pastFour[1], pastFour[2], pastFour[3]) in listOfAllValues: 
                    listOfAllValues[(pastFour[0], pastFour[1], pastFour[2], pastFour[3])] += num%10
                else:
                    listOfAllValues[(pastFour[0], pastFour[1], pastFour[2], pastFour[3])] = num%10
                valuesUsed.add((pastFour[0], pastFour[1], pastFour[2], pastFour[3]))
                
        
    total += num
curMax = -1
for v in listOfAllValues.values():
    if v > curMax:
        curMax = v
print(total)
print(curMax)





