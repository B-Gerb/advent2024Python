infoF = open('day7Info.txt', 'r')
lines = infoF.readlines()
def final(toRet, values, position, type, value, goal):
    if(value < goal):
        if(position+1 == len(values)):
            if(type == "a"):
                toRet.append(value+values[position])
            elif(type == "m"):
                toRet.append(value*values[position])
            else:
                toRet.append(int(str(value) + str(values[position])))
            return
        if(type == "a"):
            value += values[position]
            final(toRet, values, position+1, "a", value, goal)
            final(toRet, values, position+1, "m", value, goal)
            final(toRet, values, position+1, "c", value, goal)

        elif(type == "m"):
            value *= values[position]
            final(toRet, values, position+1, "a", value, goal)
            final(toRet, values, position+1, "m", value, goal)
            final(toRet, values, position+1, "c", value, goal)
        else:
            value = int(str(value) + str(values[position]))
            final(toRet, values, position+1, "a", value, goal)
            final(toRet, values, position+1, "m", value, goal)
            final(toRet, values, position+1, "c", value, goal)





total = 0
for i in lines:
    goal = int(i.split(":")[0])
    values = i.split(":")[1].strip().split(" ")
    values = [int(x) for x in values]
    toRet = []
    final(toRet, values, 1, "a", values[0], goal)
    final(toRet, values, 1, "m", values[0], goal)
    final(toRet, values, 1, "c", values[0], goal)

    if goal in toRet:
        total += goal

print(total)

