total = 0
digits = {"one":'1',"two":'2',"three":'3',"four":'4',"five":'5',"six":'6',"seven":'7',"eight":'8',"nine":'9'}


#with open("2023\Day1\input.txt") as f:
with open("2023\Day1\partTwoInput.txt") as f:
  for line in f:
    # if line == '\n' or line == "":
    
    numberList = []
    
    for index, char in enumerate(line):
        if char.isnumeric():
            numberList.append(char)
            continue

        for digit in digits:
            end = len(digit) + index
            testDigit = line[index:end]
            if testDigit in digits:
                numberList.append(digits[testDigit])
                break

    if len(numberList)==1:
        stringNumber = numberList[0] + numberList[0]
    else:
        stringNumber = numberList[0] + numberList[-1]
    num = int(stringNumber)
    print("Value: ", num)
    total = total+ num
    




print ("Total: ", total)