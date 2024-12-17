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

blanks = [i for i,x in enumerate(newString) if x == "."]
first = blanks.pop(0)
while blanks and first < len(newString):
    while newString[-1] == ".":
        del newString[-1]
    newString[first] = newString[-1]
    del newString[-1]
    first = blanks.pop(0)
total = 0
for i in range(len(newString)):
    if newString[i] == ".":
        break
    total += (i*int(newString[i]))
print(total)
infoF.close
    


infoF = open('day9Info.txt', 'r')
filesValues = {} #key is file id and value is a tuple of (spot, length)
blanks = []
spot = 0
fileId = 0
for i in range(len(val)):
    intAmt = int(val[i:i+1])
    if i%2 == 0:
        filesValues[fileId] =  (spot, intAmt)
        fileId +=1
    else:
        blanks.append((spot, intAmt))
    spot += intAmt
change = True
fileId -=1
while filesValues[fileId][0] > blanks[0][0]:
    fileToChange = filesValues[fileId] 
    spot = 0
    while spot < len(blanks) and blanks[spot][0] < filesValues[fileId][0] and blanks[spot][1] < filesValues[fileId][1]:
        spot += 1
    if spot == len(blanks) or blanks[spot][0] > filesValues[fileId][0]:
        fileId -= 1
        continue
    else:
        remain  = blanks[spot][1] - fileToChange[1]
        filesValues[fileId] = (blanks[spot][0], fileToChange[1])
        if remain > 0:
            blanks[spot] = (blanks[spot][0] + fileToChange[1], remain)
        else:
            del blanks[spot]
    fileId -= 1
total = 0
for number, (spot, amount) in filesValues.items():
    total += sum(range(spot, spot+amount))*number
print(total)
infoF.close