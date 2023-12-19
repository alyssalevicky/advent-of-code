total = 1
seps = (' ', ';', ',', ':')
time =''
distance = ''

with open("2023\Day6\input6.txt") as f:
    for index, game in enumerate(f):
        #CREATE A LIST OF WORDS
        txt = game
        default_sep = seps[0]

        # we skip seps[0] because that's the default separator
        for sep in seps[1:]:
            txt = txt.replace(sep, default_sep)
        list = [i.strip() for i in txt.split(default_sep)]

        if index == 0:
            for t in list:
                if t  != '' and t != "Time":
                    time = time + t
            
        else:
            for d in list:
                if d  != '' and d != "Distance":
                    distance = distance + d

    print ("Time ", time, " Distance: ", distance)

    #for index, t in enumerate(time):
    successCount = 0
    t = int(time)
    for x in range(0,t):
        travel = x * (t-x)

        if travel > int(distance):
            successCount += 1

    total *= successCount

    print ("Game ", t, " Success: ", successCount)


print ("Total: ", total)
