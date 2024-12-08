infoF = open('day8Info.txt', 'r')
infoF = infoF.readlines()
lines = []
dictVal = {}
values = set([])
total = 0

for i in infoF:
    lines.append(list(i.strip()))
for i in range(len(lines)):
    for v in range(len(lines[0])):
        charV = lines[i][v]
        if charV != '.':
            if(not (i,v) in values):
                total +=1
            values.add((i,v))
            
            if charV in dictVal:
                dictVal.get(charV).append((i, v))
            else:
                dictVal[charV] = [(i,v)]
for i in dictVal.items():
    val = i[1]
    for j in range(len(val)-1):
        for k in range(j+1, len(val)):
            numX = val[j][0]-val[k][0]
            numY = val[j][1]-val[k][1]
            first = (val[j][0]+numX, val[j][1]+numY)
            second = (val[k][0]-numX, val[k][1]-numY)


            while(0 <= first[0] < len(lines[0]) and 0 <= first[1] < len(lines)):
                if(not first in values):
                    total +=1
                values.add(first)

                first = (first[0]+numX, first[1]+numY)
            while(0 <= second[0] < len(lines[0]) and 0 <= second[1] < len(lines)):
                if(not second in values):
                    total +=1
                values.add(second)

                second = (second[0]-numX, second[1]-numY)

print(total)           


        
