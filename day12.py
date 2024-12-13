infoF = open('day12Info.txt', 'r')
values = infoF.readlines()
value = []
usedValues = set()
def nearby(cords, charcter, setOfValues):
    setOfValues.add(cords)
    if ((cords[0]-1, cords[1]) not in setOfValues) and cords[0] >0 and value[cords[0]-1][cords[1]] == charcter:
        nearby((cords[0]-1,cords[1]), charcter, setOfValues)
    if ((cords[0]+1, cords[1]) not in setOfValues) and cords[0] < len(value)-1 and value[cords[0]+1][cords[1]] == charcter:
        nearby((cords[0]+1,cords[1]), charcter, setOfValues)
    if ((cords[0], cords[1]-1) not in setOfValues) and cords[1] > 0 and value[cords[0]][cords[1]-1] == charcter:
        nearby((cords[0],cords[1]-1), charcter, setOfValues)
    if ((cords[0], cords[1]+1) not in setOfValues) and cords[1] < len(value[0])-1 and value[cords[0]][cords[1]+1] == charcter:
        nearby((cords[0],cords[1]+1), charcter, setOfValues)
    return setOfValues



for i in values:
    value.append(list(i.strip()))
total = 0
for i, lineValue in enumerate(value):
    for j, charValue in enumerate(lineValue):
        if (i,j) not in usedValues:
            numbersToUse = nearby((i,j), charValue, set())
            perm  = 0
            for used in numbersToUse: 
                perm+=4
                usedValues.add(used)
                if (used[0], used[1] + 1) in numbersToUse:
                    perm -=1 
                if (used[0], used[1] - 1) in numbersToUse:
                    perm -=1    
                if (used[0]+1, used[1]) in numbersToUse:
                    perm -=1   
                if (used[0]-1, used[1]) in numbersToUse:
                    perm -=1
            total += (perm*len(numbersToUse))    



print(total)

usedValues = set()
total = 0
for i, lineValue in enumerate(value):
    for j, charValue in enumerate(lineValue):
        if (i,j) not in usedValues:
            numbersToUse = nearby((i,j), charValue, set())
            up = set()
            down = set()
            left = set()
            right = set()
            sides = 0

            for v in numbersToUse:
                usedValues.add(v)

                if v not in up and (v[0]-1, v[1]) not in numbersToUse:
                    sides+=1
                    up.add(v)
                    newV = (v[0]+1,v[1])
                    while newV in numbersToUse:
                        up.add(newV)
                        newV = (newV[0]+1,newV[1])
                    newV = (v[0],v[1]+1)
                    while newV in numbersToUse and (newV[0]-1,newV[1]) not in numbersToUse:
                        up.add(newV)
                        newV = (newV[0],newV[1]+1)
                    newV = (v[0],v[1]-1)
                    while newV in numbersToUse and (newV[0]-1,newV[1]) not in numbersToUse:
                        up.add(newV)
                        newV = (newV[0],newV[1]-1)    
                if v not in down and (v[0]+1, v[1]) not in numbersToUse:
                    sides+=1
                    down.add(v)
                    newV = (v[0]-1,v[1])
                    while newV in numbersToUse:
                        down.add(newV)
                        newV = (newV[0]-1,newV[1])

                    newV = (v[0],v[1]+1)
                    while newV in numbersToUse and (newV[0]+1,newV[1]) not in numbersToUse:
                        down.add(newV)
                        newV = (newV[0],newV[1]+1)
                    newV = (v[0],v[1]-1)
                    while newV in numbersToUse and (newV[0]+1,newV[1]) not in numbersToUse:
                        down.add(newV)
                        newV = (newV[0],newV[1]-1)  
                if v not in left and (v[0], v[1]-1) not in numbersToUse:
                    sides+=1
                    left.add(v)
                    newV = (v[0],v[1]+1)
                    while newV in numbersToUse:
                        left.add(newV)
                        newV = (newV[0],newV[1]+1)

                    newV = (v[0]-1,v[1])
                    while newV in numbersToUse and (newV[0],newV[1]-1) not in numbersToUse:
                        left.add(newV)
                        newV = (newV[0]-1,newV[1])

                    newV = (v[0]+1,v[1])
                    while newV in numbersToUse and (newV[0],newV[1]-1) not in numbersToUse:
                        left.add(newV)
                        newV = (newV[0]+1,newV[1])                    

                if v not in right and (v[0], v[1]+1) not in numbersToUse:
                    sides+=1
                    right.add(v)
                    newV = (v[0],v[1]-1)
                    while newV in numbersToUse:
                        right.add(newV)
                        newV = (newV[0],newV[1]-1)

                    newV = (v[0]-1,v[1])
                    while newV in numbersToUse and (newV[0],newV[1]+1) not in numbersToUse:
                        right.add(newV)
                        newV = (newV[0]-1,newV[1])

                    newV = (v[0]+1,v[1])
                    while newV in numbersToUse and (newV[0],newV[1]+1) not in numbersToUse:
                        right.add(newV)
                        newV = (newV[0]+1,newV[1])    
            total+= sides*len(numbersToUse)            
print(total)           





