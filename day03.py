def findNums(line, lineLength):
  nums = []
  newNum = True
  num = 0
  start = -1
  end = -1
  for i in range (lineLength):
    if (line[i].isnumeric()):
      if newNum:
        start = i
      num = (num * 10) + int(line[i])
      newNum = False
    else:
      if not newNum:
        end = i - 1
        nums.append([num, start, end])
      newNum = True
      num = 0
  if not newNum:
    nums.append([num, start, lineLength - 1])
  return nums

def isPartNumEdge(toCheck, adjacent, start, end):
  if start != 0: 
    if toCheck[start - 1] != '.' or adjacent[start - 1] != '.':
      return True
  if end != len(toCheck) - 1:
    if toCheck[end + 1] != '.' or adjacent[end + 1] != '.':
      return True
  for i in range(start, end + 1):
    if adjacent[i] != '.':
      return True
  return False

def isPartNumMid(lines, start, end):
  if start != 0:
    for i in range(3):
      if lines[i][start - 1] != '.':
        return True
  if end != len(lines[0]) - 1:
    for i in range(3):
      if lines[i][end + 1] != '.':
        return True
  for i in range(start, end + 1):
    if lines[0][i] != '.' or lines[2][i] != '.':
      return True
  return False

sumOfParts = 0
with open("data/day03.txt") as f:
  first = f.readline().rstrip('\n')
  second = f.readline().rstrip('\n')

  lineLength = len(first)
  nums = findNums(first, lineLength)
  for num in nums:
    if isPartNumEdge(first, second, num[1], num[2]):
      sumOfParts += num[0]

  third = f.readline().rstrip('\n')
  lineSet = [first, second, third]

  for line in f:
    nums = findNums(lineSet[1], lineLength)
    for num in nums:
      if isPartNumMid(lineSet, num[1], num[2]):
        sumOfParts += num[0]
    nextLine = line.rstrip('\n')
    lineSet = [lineSet[1], lineSet[2], nextLine]
  
  nums = findNums(lineSet[1], lineLength)
  for num in nums:
    if isPartNumMid(lineSet, num[1], num[2]):
      sumOfParts += num[0]

  nums = findNums(lineSet[2], lineLength)
  for num in nums:
    if isPartNumEdge(lineSet[2], lineSet[1], num[1], num[2]):
      sumOfParts += num[0]
print(sumOfParts)