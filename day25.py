infoF = open("day25Info.txt", "r")
infoF = infoF.readlines()
infoF.append("")
locks = []
keys = []
part = []
for line in infoF:
    line = line.strip()
    if line == "":
        isKey = part[0][0] == '.'
        toAppend = []
        for i in range(0, len(part)):
            toAppend.append(part[i].count('#')-1)
        if isKey:
            keys.append(toAppend)
        else:
            locks.append(toAppend)    
        part = []
    else:
        for i,c in enumerate(line):
            if len(part) ==i:
                part.append("")
            part[i] += c
fit = 0
for key in keys:
    for lock in locks:
        good = True
        for i in range(0, len(key)):
            if key[i] + lock[i] > 5:
                good = False
                break
        if good:
            fit += 1
print(fit)