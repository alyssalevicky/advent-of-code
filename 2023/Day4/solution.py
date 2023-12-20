total = 0
seps1 = (':', '|')
seps2 = (' ')
copyCards = ['0']

with open("2023\Day4\input.txt") as f:
  for game in f:
    

    #CREATE A LIST OF SETS
    txt = game
    default_sep = seps1[0]

    # we skip seps[0] because that's the default separator
    for sep in seps1[1:]:
        txt = txt.replace(sep, default_sep)
    cardList = [i.strip() for i in txt.split(default_sep)]


    #SPLIT EACH GAME
    winString = cardList[1]
    default_sep = seps2[0]

    # we skip seps[0] because that's the default separator
    for sep in seps2[1:]:
        winString = winString.replace(sep, default_sep)
    winning = [i.strip() for i in winString.split(default_sep)]

    actualString = cardList[2]
    default_sep = seps2[0]

    # we skip seps[0] because that's the default separator
    for sep in seps2[1:]:
        actualString = actualString.replace(sep, default_sep)
    actual = [i.strip() for i in actualString.split(default_sep)]


    #Part 1
    # gameScore = 0
    # for index, number in enumerate(actual):
    #     if number == "":
    #        continue
    #     if number in winning:
    #         if gameScore > 0 :
    #           gameScore = gameScore*2
    #         else:
    #           gameScore = 1

    # print (cardList[0], ", Game Total: ", gameScore)
    # total = total + gameScore

    #PART 2
    
    loop = 0
    if len(copyCards) > 0:
        loop = int(copyCards[0])

    count = 0
    for index, number in enumerate(actual):
        if number == "":
           continue
        if number in winning:
            count += 1


    for x in range(1, count+1):
       if x > len(copyCards)-1:
            copyCards.append(1+loop)
       else:   
            copyCards[x] = 1 + copyCards[x] + loop

    cardCopies = 1 + loop
    if len(copyCards) > 0:
        copyCards.pop(0)

    print (cardList[0], ", Additional Card Copies: ", count, "Add to Total: ", cardCopies)

    total = total + cardCopies

    # #CHECK IF VALUES ARE WITHIN A GAME   
    # if red <= maxRed and green <= maxGreen and blue <= maxBlue:
    #    total += int(game)
    




print ("Total: ", total)
