infoF = open('day14Info.txt', 'r')
#101 tiles wide
#103 tiles tall
def location(width, tall, robot, time):
    x=((robot[2]*time+robot[0])%width)
    y=((robot[3]*time+robot[1])%tall)
    return x,y
infoF = infoF.readlines()
robots = []
wide = 101
tall = 103
q1,q2,q3,q4 = 0,0,0,0
for rob in infoF:
    parts = rob.strip().split(" ")
    position = parts[0].split("=")[1]
    velocity = parts[1].split("=")[1]
    p1,p2 = int(position.split(",")[0]),int(position.split(",")[1])
    v1,v2 = int(velocity.split(",")[0]),int(velocity.split(",")[1])
    robot = [p1,p2,v1,v2]
    robots.append(robot)
    # x,y = location(wide, tall, robot, 100)
    # if(x<100/2 and y <102/2): q1 +=1
    # if(x>100/2 and y <102/2): q2 +=1
    # if(x<100/2 and y >102/2): q3 +=1
    # if(x>100/2 and y >102/2): q4 +=1

min_val = float("inf")
time = -1
for second in range(wide*tall):
    q1,q2,q3,q4 = 0,0,0,0

    for rob in robots:
        x,y = location(wide, tall, rob, second)
        if(x<100/2 and y <102/2): q1 +=1
        if(x>100/2 and y <102/2): q2 +=1
        if(x<100/2 and y >102/2): q3 +=1
        if(x>100/2 and y >102/2): q4 +=1
    if(min_val>q1*q2*q3*q4):
        time = second
        min_val = q1*q2*q3*q4
print(time)
