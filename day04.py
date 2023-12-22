FILENAME = "data/day04.txt"

# Part 1
with open(FILENAME) as f:
  totalPoints = 0
  for line in f:
    _, card = line.rstrip('\n').split(": ")
    winning, have = card.split(" | ")
    winningNums = [int(num) for num in winning.split()]
    haveNums = [int(num) for num in have.split()]
    count = 0
    for num in haveNums:
      if num in winningNums:
        count += 1
    if (count > 0):
      totalPoints += 2**(count - 1)
  print(f'Part 1: {totalPoints}')

# Part 2
with open(FILENAME) as f:
  totalCards = 0
  instances = []
  for line in f:
    cardInstances = 1
    if len(instances) != 0:
      cardInstances += instances.pop(0)
    totalCards += cardInstances
    card, values = line.rstrip('\n').split(": ")
    card = card.strip("Card ")
    winning, have = values.split(" | ")
    winningNums = [int(num) for num in winning.split()]
    haveNums = [int(num) for num in have.split()]
    matches = 0
    for num in haveNums:
      if num in winningNums:
        if len(instances) > matches:
          instances[matches] += cardInstances
        else:
          instances.append(cardInstances)
        matches += 1
  print(f'Part 2: {totalCards}')