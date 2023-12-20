
seps = (' ', '=', ',', '(',')')
network = []
directions = []

nextSteps = []
totalSteps = 0

with open("2023\Day8\input.txt") as f:
    for line in f:
        line = line.strip()

        txt = line
        default_sep = seps[0]

        # we skip seps[0] because that's the default separator
        for sep in seps[1:]:
            txt = txt.replace(sep, default_sep)
        list = [i.strip() for i in txt.split()]

        if len(list) > 1 and list[0][2]=='A':
            nextSteps.append(list[0])

        network.append(list)

directionsToSplit = network.pop(0)[0]

for dir in directionsToSplit:
    directions.append(dir)

network.pop(0) #blank line

stop = False
directionsIndex = 0
while (not stop):
    dir = directions[directionsIndex]

    for i, step in enumerate(nextSteps):
        for item in network:
            if  item[0] == step:
                if dir == 'R':
                    nextSteps[i] = item[2]
                else:
                    nextSteps[i] = item[1]
                break
    totalSteps += 1
    
    print ("Next Steps: ", nextSteps, " Num Steps: ", totalSteps)

    directionsIndex +=1
    if directionsIndex >=  len(directions):
        directionsIndex = 0
    
    for step in nextSteps:
        if step[2] != 'Z':
            stop = False
            break
        else:
            stop = True



print ("Number of Steps: ", totalSteps)