maxCalories = 0
maxReindeer = 0
currentReindeer = 1
currentCalories = 0

with open("/Users/Alyssa.Levicky/Documents/GitHub/advent-of-code/2022/Day1/input.txt") as f:
  for line in f:
    if line == '\n' or line == "":
        if currentCalories > maxCalories:
            maxCalories = currentCalories
            maxReindeer = currentReindeer

        currentReindeer = currentReindeer + 1
        currentCalories = 0

    else:
        num = int(line.strip())
        currentCalories = currentCalories + num


print ("Max Reinder: ",maxReindeer, "Max Calories: ", maxCalories)