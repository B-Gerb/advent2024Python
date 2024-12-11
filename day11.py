from functools import cache
infoF = open("day11Info.txt", "r")

infoF = infoF.readline().split(" ")
copyValues = infoF.copy()

@cache
def count(val, steps):

    if steps == 0:
        return 1
    if val == "0":
        return count("1", steps-1)
    if len(val)%2 == 0:
        return count(val[0:len(val)//2], steps-1) + count(str(int(val[len(val)//2:])), steps-1)
    
    return count(str(int(val)*2024), steps-1)


total = 0
for i in copyValues:
    total += count(i, 75)
print(total)


        
