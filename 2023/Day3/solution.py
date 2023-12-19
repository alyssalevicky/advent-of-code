total = 0
maxRed = 12
maxGreen = 13
maxBlue = 14
seps = (',', ';', ' ', ':')


with open("2023\Day3\input.txt") as f:
  rows = len(f)
  cols = len(f[0])
  arr = [[0]*cols]*rows
  for game in f:
    
    #CREATE A LIST OF WORDS
    txt = game
    default_sep = seps[0]

    # we skip seps[0] because that's the default separator
    for sep in seps[1:]:
        txt = txt.replace(sep, default_sep)
    characterList = [i.strip() for i in txt.split(default_sep)]


    #DO SOMETHING WITH THE WORDS
    red = 0
    green = 0
    blue = 0
    fail = False

    game = characterList[1]

    #Part 1
    # for index, word in enumerate(characterList):
    #     if fail == True:
    #        continue;

    #     if word == "red" and int(characterList[index-1]) > maxRed:
    #        fail = True
    #     if word == "green" and int(characterList[index-1]) > maxGreen:
    #        fail = True
    #     if word == "blue" and int(characterList[index-1]) > maxBlue:
    #        fail = True

    # if fail == False:
    #     total += int(game)

    #Part 2
    for index, word in enumerate(characterList):
       
        if word == "red" and int(characterList[index-1]) > red:
           red = int(characterList[index-1])
        if word == "green" and int(characterList[index-1]) > green:
           green = int(characterList[index-1])
        if word == "blue" and int(characterList[index-1]) > blue:
           blue = int(characterList[index-1])

    total = total + (red*green*blue)

    # #CHECK IF VALUES ARE WITHIN A GAME   
    # if red <= maxRed and green <= maxGreen and blue <= maxBlue:
    #    total += int(game)
    




print ("Total: ", total)
