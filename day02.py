lines = []
with open("data/day02.txt") as f:
  lines = f.readlines()

# Part 1
RED_CUBES = 12
GREEN_CUBES = 13
BLUE_CUBES = 14

validIdSum = 0
for game in lines:
  if game[len(game) - 1] == '\n':
    game = game[:len(game) - 1]
  gameNum, rounds = game.split(": ", 1)
  gameNum = int(gameNum[5:])
  rounds = rounds.split("; ")

  isValid = True
  for round in rounds:
    cubes = round.split(", ")
    for cube in cubes:
      num, color = cube.split(" ", 1)
      num = int(num)
      if color == "red" and num > RED_CUBES:
        isValid = False
        break
      elif color == "blue" and num > BLUE_CUBES:
        isValid = False
        break
      elif color == "green" and num > GREEN_CUBES:
        isValid = False
        break
  if isValid:
    validIdSum = validIdSum + gameNum

print(validIdSum)

# Part 2
totalPower = 0
for game in lines:
  if game[len(game) - 1] == '\n':
    game = game[:len(game) - 1]
  gameNum, rounds = game.split(": ", 1)
  rounds = rounds.split("; ")
  minRed = 0
  minGreen = 0
  minBlue = 0
  for round in rounds:
    cubes = round.split(", ")
    for cube in cubes:
      num, color = cube.split(" ", 1)
      num = int(num)
      if color == "red" and num > minRed:
        minRed = num
      elif color == "blue" and num > minBlue:
        minBlue = num
      elif color == "green" and num > minGreen:
        minGreen = num
  totalPower = totalPower + (minRed * minBlue * minGreen)

print(totalPower)
