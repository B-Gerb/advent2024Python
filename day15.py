# infoF = open('day15Info.txt', 'r')

# infoF = infoF.readlines()
# lines = []

# command = False
# commands = ""
# for i,stringValue in enumerate(infoF):
#     if stringValue == "\n":
#         command = True
#     else: 
#         if(command):
#             commands += stringValue.strip()
#         else:
#             temp = []
#             for j, char in enumerate(stringValue.strip()):
#                 if char == "@":
#                     x,y = i,j

#                 temp.append(char)
#             lines.append(temp)

# def simulate(lines, x, y, commands):
#     for command in commands.strip():
#         x,y = move(lines, x, y, command)
            
        
# def move(lines, x, y, command):
#     if command == "^":
#         if x-1 <= 0 or lines[x-1][y] == "#": return x,y
#         if lines[x-1][y] == ".":
#             lines[x][y] = "."
#             lines[x-1][y] = '@'
#             return x-1,y
#         if lines[x-1][y] == "O":
#             foundBlank = False
#             val = x-1
#             while val >= 0 and not foundBlank:
#                 if lines[val][y] == "#":
#                     return x,y
#                 if lines[val][y] == ".":
#                     foundBlank = True
#                     break
#                 val -= 1
#             lines[x][y] = "."
#             lines[x-1][y] = '@'
#             lines[val][y] = "O"
#             return x-1,y

#     elif command == "v":
#         if x+1 >= len(lines) or lines[x+1][y] == "#": return x,y
#         if lines[x+1][y] == ".":
#             lines[x][y] = "."
#             lines[x+1][y] = '@'
#             return x+1,y        
#         if lines[x+1][y] == "O":
#             foundBlank = False
#             val = x+1
#             while val < len(lines) and not foundBlank:
#                 if lines[val][y] == "#":
#                     return x,y
#                 if lines[val][y] == ".":
#                     foundBlank = True
#                     break
#                 val += 1
#             lines[x][y] = "."
#             lines[x+1][y] = '@'
#             lines[val][y] = "O"
#             return x+1,y
#     elif command == ">":
#         if y+1 >= len(lines[0]) or lines[x][y+1] == "#": return x,y
#         if lines[x][y+1] == ".":
#             lines[x][y] = "."
#             lines[x][y+1] = '@'
#             return x,y+1
#         if lines[x][y+1] == "O":
#             foundBlank = False
#             val = y+1
#             while val < len(lines[0]) and not foundBlank:
#                 if lines[x][val] == "#":
#                     return x,y
#                 if lines[x][val] == ".":
#                     foundBlank = True
#                     break
#                 val += 1
#             lines[x][y] = "."
#             lines[x][y+1] = '@'
#             lines[x][val] = "O"
#             return x,y+1
#     elif command == "<":
#         if y-1 <= 0 or lines[x][y-1] == "#": return x,y
#         if lines[x][y-1] == ".":
#             lines[x][y] = "."
#             lines[x][y-1] = '@'
#             return x,y-1
#         if lines[x][y-1] == "O":
#             foundBlank = False
#             val = y-1
#             while val >= 0 and not foundBlank:
#                 if lines[x][val] == "#":
#                     return x,y
#                 if lines[x][val] == ".":
#                     foundBlank = True
#                     break
#                 val -= 1
#             lines[x][y] = "."
#             lines[x][y-1] = '@'
#             lines[x][val] = "O"
#             return x,y-1            
        
# total = 0
# simulate(lines, x, y, commands)
# for i,line in enumerate(lines):
#     for j, char in enumerate(line):
#         if char == "O":
#             total += (i)*100+(j)
    
# print(total)


# part 2
infoF = open('day15Info.txt', 'r')

infoF = infoF.readlines()
lines = []

command = False
commands = ""
for i,stringValue in enumerate(infoF):
    if stringValue == "\n":
        command = True
    else: 
        if(command):
            commands += stringValue.strip()
        else:
            temp = []
            for j, char in enumerate(stringValue.strip()):
                if char == "@":
                    x,y = i,j*2
                    temp.append('@')
                    temp.append(".")

                elif char == "O":
                    temp.append("[")
                    temp.append("]")
                else:
                    temp.append(char)
                    temp.append(char)

            lines.append(temp)

def simulate(lines, x, y, commands):
    for command in commands.strip():
        x,y = move(lines, x, y, command)


def move(lines, x, y, command):

    if command == "v":
        move = True
        values = [[x,y]]
        for value in values:
            if lines[value[0]+1][value[1]] == "#":
                move = False
                break
            if lines[value[0]+1][value[1]] == "[" and [value[0]+1, value[1]] not in values:
                values.append([value[0]+1, value[1]+1])
                values.append([value[0]+1, value[1]])
            if lines[value[0]+1][value[1]] == "]" and [value[0]+1, value[1]] not in values:
                values.append([value[0]+1, value[1]-1])
                values.append([value[0]+1, value[1]])
        if move:
            copyGrid = [x[:] for x in lines]
            for value in values:
                lines[value[0]][value[1]] = "."
            for value in values:
                lines[value[0]+1][value[1]] = copyGrid[value[0]][value[1]]
            return x+1,y
        return x,y

    elif command == "^":
        move = True
        values = [[x,y]]
        for value in values:
            if lines[value[0]-1][value[1]] == "#":
                move = False
                break
            if lines[value[0]-1][value[1]] == "[" and [value[0]-1, value[1]] not in values:
                values.append([value[0]-1, value[1]+1])
                values.append([value[0]-1, value[1]])
            if lines[value[0]-1][value[1]] == "]" and [value[0]-1, value[1]] not in values:
                values.append([value[0]-1, value[1]-1])
                values.append([value[0]-1, value[1]])
        if move:
            copyGrid = [x[:] for x in lines]
            for value in values:
                lines[value[0]][value[1]] = "."
            for value in values:
                lines[value[0]-1][value[1]] = copyGrid[value[0]][value[1]]
            return x-1,y
        return x,y
    elif command == ">":
        if y+1 >= len(lines[0]) or lines[x][y+1] == "#": return x,y
        if lines[x][y+1] == ".":
            lines[x][y] = "."
            lines[x][y+1] = '@'
            return x,y+1
        if lines[x][y+1] == "[":
            foundBlank = False
            val = y+1
            while val < len(lines[0]) and not foundBlank:
                if lines[x][val] == "#":
                    return x,y
                if lines[x][val] == ".":
                    foundBlank = True
                    break
                val += 1
            del lines[x][val]
            lines[x].insert( y, '.')
            return x,y+1
        return x,y
    elif command == "<":
        if y-1 <= 0 or lines[x][y-1] == "#": return x,y
        if lines[x][y-1] == ".":
            lines[x][y] = "."
            lines[x][y-1] = '@'
            return x,y-1
        if lines[x][y-1] == "]":
            foundBlank = False
            val = y-1
            while val >= 0 and not foundBlank:
                if lines[x][val] == "#":
                    return x,y
                if lines[x][val] == ".":
                    foundBlank = True
                    break
                val -= 1
            del lines[x][val]
            lines[x].insert( y, '.')
            return x,y-1 
        return x,y           
        
total = 0
simulate(lines, x, y, commands)
for i,line in enumerate(lines):
    for j, char in enumerate(line):
        if char == "[":
            total += (i)*100+(j)
    
print(total)

