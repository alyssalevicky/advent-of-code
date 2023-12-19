total = 0
digits = ["one","two","three","four","five","six","seven","eight","nine"]


#with open("2023\Day1\input.txt") as f:
with open("2023\Day1\partTwoInput.txt") as f:
  for line in f:
    # if line == '\n' or line == "":
    
    characterList = list(line)
    numberList = list()
    
    place = 0
    for item in characterList:
        try:
            number = int(item)
            numberList.append( str(number))
            place += 1
        except ValueError:
            for digit in digits:
                testString = ""
                digitLength = len(digit)
                
    

    if len(numberList)==1:
        stringNumber = numberList[0] + numberList[0]
    else:
        stringNumber = numberList[0] + numberList[-1]
    num = int(stringNumber)
    print("Value: ", num)
    total = total+ num
    




print ("Total: ", total)