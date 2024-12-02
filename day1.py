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
for l,r in zip(leftValue, rightValue):
    differences+= abs(l-r)

print(differences)


infoF.close()