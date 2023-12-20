hasSpecialChar = False

def is_special_char(char):
    if not str(char).isnumeric() and char != '.':
        return True
    return False

def is_valid_char(char):
    return char != '.'  # Periods do not count as a symbol

def is_part_number(engine, row, col):
    # Check adjacent cells (including diagonals) for symbols
    isNumber = False
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue  # Skip the current cell
            new_row, new_col = row + i, col + j
            if 0 <= new_row < len(engine) and 0 <= new_col < len(engine[0]):
                var = engine[new_row][new_col]
                if is_valid_char(var):
                    if is_special_char(var):
                        global hasSpecialChar
                        hasSpecialChar = True
                    isNumber = True
    return isNumber

def sum_part_numbers(engine):
    sum = 0
    num = ''
    for row_idx, row in enumerate(engine):
        for col_idx, char in enumerate(row):
            if char.isdigit() and is_part_number(engine, row_idx, col_idx):
                num += char
                #sum += int(char)
            if (char == '.' or not char.isnumeric()) and num != '':
               global hasSpecialChar
               numericNum = int(num)
               if hasSpecialChar == True:
                  print ("Number adding: ", numericNum)
                  sum += numericNum
               num = ''
               hasSpecialChar = False
    return sum

# Your engine schematic (replace this with your actual input)
engine_schematic = []

with open("2023\Day3\input.txt") as f:
  for game in f:
      engine_schematic.append(game.strip())

# Calculate the sum of all part numbers
result = sum_part_numbers(engine_schematic)
print("Sum of all part numbers:", result)