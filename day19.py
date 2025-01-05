possibilies = []
memorize = {}
infoF = open("day19Info.txt", "r")
infoF = infoF.readlines()
first = True
part1 = 0
part2 = 0
def check(tester):
    if tester in memorize:
        return memorize[tester]
    if len(tester) == 0:
        return 1
    amt = 0
    for i in possibilies:
        if tester.startswith(i):
            amt += check(tester[len(i):])
    memorize[tester] = amt
    return amt
for line in infoF:
    if first:
        first = False
        line = line.strip()
        possibilies = line.split(", ")
    else:
        line = line.strip()
        if line:
            val = check(line)
            part2 += val
            if val >0:
                part1 += 1
print(part1, part2)