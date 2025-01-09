values = {}
xValues = []
yValues = []
infoF = open("day24Info.txt", "r")
infoF = infoF.readlines()
commands = False
allCommands = {}
zValues = []

for line in infoF:
    line = line.strip()
    if line == "":
        commands = True
        continue
    if commands:
        parts = line.replace(" -> ", " ").split(" ")
        allCommands[parts[3]] = parts[0:-1]
        if parts[3].startswith("z"):
            zValues.append(parts[3])

    else:
        parts = line.split(": ")
        if parts[0].startswith("x"):
            xValues.append(parts[0])
        elif parts[0].startswith("y"):
            yValues.append(parts[0])
        values[parts[0]] = int(parts[1])

functions = {
    "AND": lambda a, b: a & b,
    "OR": lambda a, b: a | b,
    "XOR": lambda a, b: a ^ b,
}

def calc(command, important):    

    if command in values:
        return values[command]
    else:
        impacted[important].append((command, allCommands[command]))
        return functions[allCommands[command][1]](calc(allCommands[command][0], important), calc(allCommands[command][2], important)) 
        # values[command] = toAdd
        return toAdd

impacted = {}
total = 0
for z in zValues:
    impacted[z] = []
    values[z] = calc(z, z)
#part 1
printAfter = ""

for x, i in enumerate(zValues):

    printAfter += str(values[i])
    total += values[i] * 2 ** (x)
#print(total, printAfter)




xTotal = 0
stopNum = 46
#11 wrong swapped wpd,z11

#15 or 16 wrong
#15 wrong SKH is x15 AND y15 should be x15 XOR Y15
# swap jqf and skh

#19 or 20 wrong

#37 or 38 wrong
#final swaps
#wpd,z11
#jqf,skh
#z19,mdd
#wts,z37
toSort = ['wpd', 'z11', 'jqf', 'skh', 'z19', 'mdd', 'wts', 'z37']
toSort.sort()
print(",".join(toSort))



for x,i  in enumerate(xValues):
    if x == stopNum:
        break
    xTotal += values[i] * 2 ** (x)
yTotal = 0
for x,i  in enumerate(yValues):
    if x == stopNum:
        break
    yTotal += values[i] * 2 ** (x)
zValues.sort()

total = 0
for x, i in enumerate(zValues):
    if x == stopNum:
        break

    printAfter += str(values[i])
    total += values[i] * 2 ** (x)
print(total, xTotal, yTotal, (xTotal+yTotal==total or xTotal + yTotal == total + (2**stopNum)))