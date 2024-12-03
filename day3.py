infoF = open('day3Info.txt', 'r')
lines = infoF.read()


while not lines.find("don't") == -1:
    if lines[lines.find("don't")+4:].find("do") == -1:
        lines = lines[0: lines.find("don't")]
    else:
        temp = lines[lines.find("don't")+4:]
        lines = lines[0: lines.find("don't")] + temp[temp.find("do"):]
partX = lines.split("mul")
total = 0


for x in partX:
    if x.startswith("(") and ")" in x:
        x = x[1:x.find(")")]
        parts  = x.split(",")
        if len(parts) == 2:
            if(parts[0].isdigit() and parts[1].isdigit()):
                total += int(parts[0]) * int(parts[1])
print(total)

infoF.close()
