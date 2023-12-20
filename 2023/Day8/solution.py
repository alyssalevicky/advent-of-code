
seps = (' ', '=', ',', '(',')')
network = []
directions = []

nextStep = 'AAA'
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

        network.append(list)

directionsToSplit = network.pop(0)[0]

for dir in directionsToSplit:
    directions.append(dir)

network.pop(0) #blank line

directionsIndex = 0
while (nextStep != 'ZZZ'):
    dir = directions[directionsIndex]

    for item in network:
        if  item[0] == nextStep:
            if dir == 'R':
                nextStep = item[2]
            else:
                nextStep = item[1]
            totalSteps += 1

            directionsIndex +=1
            if directionsIndex >=  len(directions):
                directionsIndex = 0
            break



print ("Number of Steps: ", totalSteps)