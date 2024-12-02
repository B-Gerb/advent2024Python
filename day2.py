

def valid(part):
    
    for i in range(len(part)-1):
        if(i==0):
            increasing = (part[i+1]-part[i])>0
        if(increasing):
            if not ( 0 < (part[i+1] - part[i]) <= 3):
                return False
        else:
            if not ( 0 > (part[i+1] - part[i]) >= -3):
                return False
    return True

infoF = open('day2Info.txt', 'r')
lines = infoF.readlines()
total = 0
for x in lines:
    part = x.split()
    increasing = False
    add = False
    change = False
    part = [int(x) for x in part]
    for i in range(len(part)+1):
        partRemove = part.copy()
        if not i == len(part):
            del partRemove[i]
        add = valid(partRemove)
        if(add):
            break

        
    if(add):
        total += 1

print(total)


infoF.close()