import os
FILENAME = "data/day03.txt"

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

# Part 1
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
with open(FILENAME) as f:
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


# Part 2
gears = {}

def addGear(num, row, column):
  if row not in gears:
    gears[row] = {}
  if column in gears[row]:
    if (gears[row][column][1]):
      gears[row][column][0] = 0
    else:
      gearRatio = gears[row][column][0] * num
      gears[row][column] = (gearRatio, True)
  else:
    gears[row][column] = (num, False)

def findBoundaryGears(nums, current, adjacent, rowNum, lineLength):
  adjacentRow = 0
  if rowNum == 0:
    adjacentRow = 1
  else:
    adjacentRow = rowNum - 1

  for num in nums:
    start = num[1]
    end = num[2] + 1
    if num[1] != 0:
      start -= 1
      if current[num[1] - 1] == '*':
        addGear(num[0], rowNum, num[1] - 1)
    if num[2] != lineLength - 1:
      end += 1
      if current[num[2] + 1] == '*':
        addGear(num[0], rowNum, num[2] + 1)
    for i in range (start, end):
      if adjacent[i] == '*':
        addGear(num[0], adjacentRow, i)

def findGears(nums, current, above, below, rowNum, lineLength):
  aboveRowNum = rowNum - 1
  belowRowNum = rowNum + 1

  for num in nums:
    start = num[1]
    end = num[2] + 1
    if num[1] != 0:
      start -= 1
      if current[num[1] - 1] == '*':
        addGear(num[0], rowNum, num[1] - 1)
    if num[2] != lineLength - 1:
      end += 1
      if current[num[2] + 1] == '*':
        addGear(num[0], rowNum, num[2] + 1)

    for i in range (start, end):
      if above[i] == '*':
        addGear(num[0], aboveRowNum, i)
      if below[i] == '*':
        addGear(num[0], belowRowNum, i)

with open(FILENAME) as f:
  first = f.readline()
  lineLength = len(first)
  fileSize = os.stat(FILENAME).st_size

  # 1 extra for last line newLine 
  fileSize += 1
  numLines = fileSize//lineLength

  first = first.rstrip('\n')
  lineLength -= 1
  nums = findNums(first, lineLength)
  nextLine = f.readline().rstrip('\n')

  findBoundaryGears(nums, first, nextLine, 0, lineLength)

  currentLine = nextLine
  aboveLine = first
  for i in range(1, numLines - 1):
    nums = findNums(currentLine, lineLength)
    belowLine = f.readline().rstrip('\n')
    findGears(nums, currentLine, aboveLine, belowLine, i, lineLength)
    aboveLine = currentLine
    currentLine = belowLine
  
  nums = findNums(currentLine, lineLength)
  findBoundaryGears(nums, currentLine, aboveLine, numLines - 1, lineLength)

gearRatioSum = 0
for row in gears.values():
  for gear in row.values():
    if gear[1]:
      gearRatioSum += gear[0]
print(gearRatioSum)