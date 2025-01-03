import math
infoF = open('day17Info.txt', 'r')
infoF = infoF.readlines()
def binaryToNum(binary):
    num = 0
    for i in range(len(binary)):
        num += binary[i] * math.pow(2, len(binary)-1-i)
    return int(num)
for line in infoF:
    line = line.strip()
    if "Register A" in line:
        A = int(line.split(": ")[1])
    if "Register B" in line:
        B = int(line.split(": ")[1])
    if "Register C" in line:
        C = int(line.split(": ")[1])

    if 'Program' in line:
        program  = [int(num) for num in line.split(': ')[1].split(",")]
values = [0, 1, 2, 3, A, B, C, 7]
idx = 0
toPrint = ''
while idx < len(program):
    command = program[idx]
    combo = values[program[idx+1]]
    if command == 0:
        A = A >> combo
        values[4] = A
    if command == 1:
        B = B ^ program[idx+1]
        values[5] = B
    if command == 2:
        B = combo%8
        values[5] = B
    if command == 3:
        if A != 0:
            idx = program[idx+1]
            continue
    if command == 4:
        B = B ^ C
        values[5] = B
    if command == 5:
        toPrint += str(combo%8) + ","
    if command == 6:
        B = A >> combo
        values[5] = B
    if command == 7:
        C = A >> combo
        values[6] = C
    idx += 2
print(toPrint[:-1])


# part 2
def test (A, B, C):
    values = [0, 1, 2, 3, A, B, C, 7]
    toPrint = []
    idx = 0
    while idx < len(program):
        command = program[idx]
        combo = values[program[idx+1]]
        if command == 0:
            A = A >> combo
            values[4] = A
        if command == 1:
            B = B ^ program[idx+1]
            values[5] = B
        if command == 2:
            B = combo%8
            values[5] = B
        if command == 3:
            if A != 0:
                idx = program[idx+1]
                continue
        if command == 4:
            B = B ^ C
            values[5] = B
        if command == 5:
            toPrint.append(combo%8)
        if command == 6:
            B = A >> combo
            values[5] = B
        if command == 7:
            C = A >> combo
            values[6] = C
        idx += 2
    return toPrint 
binaryValue = [1,1,0,1,0,1,1,1,0,0,1,0]
result = test(binaryToNum(binaryValue), 0, 0)
values = {}
values[0] = [0,0,0]
values[1] = [0,0,1]
values[2] = [0,1,0]
values[3] = [0,1,1]
values[4] = [1,0,0]
values[5] = [1,0,1]
values[6] = [1,1,0]
values[7] = [1,1,1]
once = True
allValues = []
minVal = float('inf')
while allValues or once:
    if(once):
        once = False
        length = 0
        binaryValue = []
    else:
        binaryValue = allValues.pop()
    length = int(len(binaryValue)/3)
    for i in range(8):
        copy = binaryValue.copy()
        copy += values.get(i)
        testAgainst = test(binaryToNum(copy), 0, 0)
        if testAgainst == program[-(length+1):]:
            allValues.append(copy)
    numberVal = binaryToNum(binaryValue)
    if program == test(numberVal, 0, 0) and numberVal < minVal:
        minVal = numberVal
print(minVal)

