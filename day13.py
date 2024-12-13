def calc(A, B, goal):
    y = (A[1]*goal[0]-A[0]*goal[1]) / (A[1]*B[0]-A[0]*B[1])
    x = (goal[0]-B[0]*y)/A[0]
    if y.is_integer() and x.is_integer():

        return x*3+y

    return -1 

infoF = open('day13Info.txt', 'r')

infoF = infoF.readlines()
total = 0
for v in infoF:
    if v == '\n':
        val = calc(A,B,goal)
        if val != -1:
            total += val
    else:
        if "Button A" in v:
            x = int(v.split(",")[0].split("+")[1])
            y = int(v.split("+")[2].strip())
            A = [x,y]
        if "Button B" in v:
            x = int(v.split(",")[0].split("+")[1])
            y = int(v.split("+")[2].strip())
            B = [x,y]
        if "Prize" in v:
            x = int(v.split("=")[1].split(",")[0])+10000000000000
            y = int(v.split("=")[2].strip())+10000000000000
            goal = [x,y]


val = calc(A,B,goal)
if val != -1:
    total += val
print(total)