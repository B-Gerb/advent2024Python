
infoF = open('day4Info.txt', 'r')
lines = infoF.readlines()
lines = [x.lower() for x in lines]

total = 0
for i in range(len(lines)):
    for y in range(len(lines[i])):
        if lines[i][y:y+1] == "x":
            if y>=3 and lines[i][y-1:y] == "m" and lines[i][y-2:y-1] == "a" and lines[i][y-3:y-2] == "s":
                total += 1
            if y<=len(lines[i])-3 and lines[i][y+1:y+2] == "m" and lines[i][y+2:y+3] == "a" and lines[i][y+3:y+4] == "s":
                total += 1
            if i >= 3:
                if y>=3:
                    if lines[i-1][y-1:y] == "m" and lines[i-2][y-2:y-1] == "a" and lines[i-3][y-3:y-2] == "s":
                        total += 1
                if y<=len(lines[i])-3:
                    if lines[i-1][y+1:y+2] == "m" and lines[i-2][y+2:y+3] == "a" and lines[i-3][y+3:y+4] == "s":
                        total += 1
                if lines[i-1][y:y+1] == "m" and lines[i-2][y:y+1] == "a" and lines[i-3][y:y+1] == "s":
                    total += 1
            if i < len(lines)-3:
                if y>=3:
                    if lines[i+1][y-1:y] == "m" and lines[i+2][y-2:y-1] == "a" and lines[i+3][y-3:y-2] == "s":
                        total += 1
                if y<=len(lines[i])-3:
                    if lines[i+1][y+1:y+2] == "m" and lines[i+2][y+2:y+3] == "a" and lines[i+3][y+3:y+4] == "s":
                        total += 1
                if lines[i+1][y:y+1] == "m" and lines[i+2][y:y+1] == "a" and lines[i+3][y:y+1] == "s":
                    total += 1            





print(total)

parttwototal = 0
for i in range(1, len(lines)-1):
    for y in range(1, len(lines[i])-1):
        if lines[i][y:y+1] == "a":
            part1 = lines[i-1][y-1:y] + lines[i][y:y+1] + lines[i+1][y+1:y+2]
            part2 = lines[i-1][y+1:y+2] + lines[i][y:y+1] + lines[i+1][y-1:y]
            if (part1 == "mas" or part1 == "sam") and (part2 == "mas" or part2 == "sam"):
                parttwototal +=1
print(parttwototal)
               
infoF.close()
