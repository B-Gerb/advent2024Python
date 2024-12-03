infoF = open('day1Info.txt', 'r')
lines = infoF.readlines()
differences =0
leftValue = []
rightValue = []
for x in lines:
    part = x.split()
    leftValue.append(int(part[0]))
    rightValue.append(int(part[1]))

leftValue.sort()
rightValue.sort()
for l,r in zip(leftValue, rightValue,):
    differences+= abs(l-r)

print(f"Part 1: {differences}")
dict = {}
for v in rightValue:
    if not (v in dict):
        dict[v] = 1
    else:
        dict[v] = dict[v]+1
total = 0 
for v in leftValue:
    if v in dict:
        total += (v*dict[v])
print(f"Part 2: {total}")
infoF.close()