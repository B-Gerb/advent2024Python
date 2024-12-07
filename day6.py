infoF = open('day6Info.txt', 'r')
lines = infoF.readlines()
linesInList = []
for i in range(len(lines)):
    linesInList.append(list(lines[i].strip()))
    if '^' in lines[i]:
        start = (i, lines[i].index('^'))
        linesInList[i][start[1]] = '.'
dir = 'up'
lines = linesInList
copyStart = (start[0], start[1])
while (start[0]  != -1) and (start[0]  != len(lines))  and (start[1]  != -1) and (start[1]  != len(lines[0])):
    lines[start[0]][start[1]] = 'X'

    if dir == 'up' :

        if start[0] == 0:
            break
        if lines[start[0]-1][start[1]] == '#':
            dir = 'right'
        else:
            start = (start[0]-1, start[1])
    elif dir == 'down':
        if start[0] == len(lines)-1:
            break
        if lines[start[0]+1][start[1]] == '#':
            dir = 'left'
        else:
            start = (start[0]+1, start[1])
    elif dir == 'left':
        if start[1] == 0:
            break
        if lines[start[0]][start[1]-1] == '#':
            dir = 'up'
        else:
            start = (start[0], start[1] -1)
    elif dir == 'right':
        if start[1] == len(lines[0])-1:
            break
        if lines[start[0]][start[1]+1] == '#':
            dir = 'down'
        else:
            start = (start[0], start[1] +1)
total = 0
for i in lines:
    for x in i:
        if x=='X':
            total +=1

print(total)
def valid(valuesX, valuesY, lines, start):
    copy = (start[0], start[1])
    dictVal = {}
    dir = 'up'
    while (copy[0]  != -1) and (copy[0]  != len(lines))  and (copy[1]  != -1) and (copy[1]  != len(lines[0])):
        if(dir == 'up'):
            good = False
            for v in range(copy[0], -1,-1):
                if copy[1] in valuesY and v in valuesY.get(copy[1]):
                    if v < copy[0]:
                        copy = (v+1, copy[1])
                        if copy in dictVal:
                            if dir in dictVal.get(copy):
                                return True
                            dictVal.get(copy).append(dir)
                        else:
                            dictVal[copy] =  [dir]
                        dir = 'right'
                        good = True
                        break
            if not good:
                return False
        elif(dir == 'down'):
            good = False
            for v in range(copy[0], len(lines)):
                if copy[1] in valuesY and v in valuesY.get(copy[1]):
                    if v > copy[0]:
                        copy = (v-1, copy[1])
                        if copy in dictVal:
                            if dir in dictVal.get(copy):
                                return True
                            dictVal.get(copy).append(dir)
                        else:
                            dictVal[copy] =  [dir]
                        dir = 'left'
                        good = True
                        break
            if not good:
                return False
        elif(dir == 'left'):
            good = False
            for v in range(copy[1], -1, -1):
                if copy[0] in valuesX and v in valuesX.get(copy[0]):
                    if v < copy[1]:
                        copy = (copy[0], v+1)
                        if copy in dictVal:
                            if dir in dictVal.get(copy):
                                return True
                            dictVal.get(copy).append(dir)
                        else:
                            dictVal[copy] =  [dir]
                        dir = 'up'
                        good = True
                        break
            if not good:
                return False
        elif(dir == 'right'):
            good = False
            for v in range(copy[1], len(lines[0])):
                if copy[0] in valuesX and v in valuesX.get(copy[0]):
                    if v > copy[1]:
                        copy = (copy[0], v-1)
                        if copy in dictVal:
                            if dir in dictVal.get(copy):
                                return True
                            dictVal.get(copy).append(dir)
                        else:
                            dictVal[copy] =  [dir]
                        dir = 'down'
                        good = True
                        break
            if not good:
                return False
    
    return False
 


valuesX = {}
valuesY = {}
dict = {}
for i in range(len(lines)):
    for var in range(len(lines[i])):
        if lines[i][var] == "#":
            if i in valuesX:
                valuesX.get(i).append(var)
            else:
                valuesX[i] = [var]
            if var in valuesY:
                valuesY.get(var).append(i)
            else:
                valuesY[var] =  [i]
part2 = 0
import copy
for i in range(len(lines)):
    for var in range(len(lines[i])):
        if(lines[i][var] == "X"):

            if(copyStart[0] !=i or copyStart[1] != var):
                copyValuesX = copy.deepcopy(valuesX)
                copyValuesY = copy.deepcopy(valuesY)


                if (i in valuesX and (not var in valuesX.get(i))):
                    copyValuesX.get(i).append(var)
                    if(var in valuesY):
                        copyValuesY.get(var).append(i)
                    else:
                        copyValuesY[var] =  [i]
                    if(valid(copyValuesX, copyValuesY, lines, copyStart)):
                        part2 += 1
                elif (not i in valuesX ):
                    copyValuesX[i] =  [var]
                    if(var in valuesY):
                        copyValuesY.get(var).append(i)
                    else:
                        copyValuesY[var] =  [i]
                    if(valid(copyValuesX, copyValuesY, lines, copyStart)):
                        part2 += 1
print(part2)



            


