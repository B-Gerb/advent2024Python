infoF = open('day5Info.txt', 'r')
lines = infoF.readlines()
dictBad ={}
forDict = True
total = 0
for i in lines:
    if len(i.strip()) == 0:
        forDict = False
    else:
        if(forDict):
            parts = i.split("|")
            if int(parts[1].strip()) in dictBad:
                dictBad.get(int(parts[1].strip())).append(int(parts[0].strip()))
            else:
                dictBad[int(parts[1].strip())] = [int(parts[0].strip())]
        else:
            parts = i.split(",")
            parts = [int(x) for x in parts]
            seenSet =  set([])
            bad= False
            newLoop = False
            k=0
            while k < len(parts):
                if(newLoop):
                    k=0
                    seenSet =  set([])
                    newLoop = False
                    continue
                val = parts[k]
                seenSet.add(val)
                if val in dictBad:
                    for x in dictBad.get(val):
                        if (not x in seenSet) and x in parts:
                            parts[parts.index(x)],parts[parts.index(val)] = parts[parts.index(val)],parts[parts.index(x)]
                            bad = True
                            newLoop = True
                            break
                k+=1                    
            if(bad):
                total += parts[int(len(parts)/2)]
            

            #part 1
            # parts = i.split(",")
            # parts = [int(x) for x in parts]
            # seenSet =  set([])
            # good= True
            # for val in parts:
            #     seenSet.add(val)
            #     if val in dictBad:
                    
            #         for x in dictBad.get(val):
            #             if (not x in seenSet) and x in parts:
            #                 good = False
            #                 break                    
            # if(good):
            #     total += parts[int(len(parts)/2)]
print(total)   


infoF.close