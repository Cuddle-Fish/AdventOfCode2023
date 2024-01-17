FILENAME = 'data/day10.txt'

def removeExterior(path, numRows, numColumns):
  tileRemoved = False
  for i in range(numRows - 1):
    for j in range(numColumns - 1):
        if (
          (path[i][j] == '.' or
           path[i][j] == 'X') and
          (path[i-1][j] == '0' or
          path[i+1][j] == '0' or
          path[i][j-1] == '0' or
          path[i][j+1] == '0')
        ):
          path[i][j] = '0'
          tileRemoved = True

  for i in reversed(range(numRows - 1)):
    for j in reversed(range(numColumns - 1)):
        if (
          (path[i][j] == '.' or
           path[i][j] == 'X') and
          (path[i-1][j] == '0' or
          path[i+1][j] == '0' or
          path[i][j-1] == '0' or
          path[i][j+1] == '0')
        ):
          path[i][j] = '0'
          tileRemoved = True
  
  return path, tileRemoved


pipes = []
startRow = 0
currentRow = 0
with open(FILENAME) as f:
  for line in f:
    pipes.append(line.rstrip())
    if 'S' in line:
      startRow = currentRow
    currentRow += 1

startColumn = pipes[startRow].find('S')
numRows = len(pipes)
numColumns = len(pipes[0])

pipeFlow = {
  '.': {},
  '-': {'W': (0, -1, 'W'), 'E': (0, 1, 'E')},
  '|': {'N': (-1, 0, 'N'), 'S': (1, 0, 'S')},
  'F': {'N': (0, 1, 'E'), 'W': (1, 0, 'S')},
  'L': {'S': (0, 1, 'E'), 'W': (-1, 0, 'N')},
  'J': {'S': (0, -1, 'W'), 'E': (-1, 0, 'N')},
  '7': {'N': (0, -1, 'W'), 'E': (1, 0, 'S')}
}

path = [['.' for _ in range(numColumns)] for _ in range(numRows)]
path[startRow][startColumn] = 'S'

currentRow = 0
currentColumn = 0

startConnections = set()

if startColumn != 0 and 'N' in pipeFlow[pipes[startRow - 1][startColumn]].keys():
  rowChange, columnChange, direction = pipeFlow[pipes[startRow - 1][startColumn]]['N']
  currentRow = startRow - 1 + rowChange
  currentColumn = startColumn + columnChange
  path[startRow - 1][startColumn] = pipes[startRow - 1][startColumn]
  startConnections.add('N')
if startRow != 0 and 'W' in pipeFlow[pipes[startRow][startColumn - 1]].keys():
  rowChange, columnChange, direction = pipeFlow[pipes[startRow][startColumn - 1]]['W']
  currentRow = startRow + rowChange
  currentColumn = startColumn - 1 + columnChange
  path[startRow][startColumn - 1] = pipes[startRow][startColumn - 1]
  startConnections.add('W')
if startRow != numRows - 1 and 'E' in pipeFlow[pipes[startRow][startColumn + 1]].keys():
  rowChange, columnChange, direction = pipeFlow[pipes[startRow][startColumn + 1]]['E']
  currentRow = startRow + rowChange
  currentColumn = startColumn + 1 + columnChange
  path[startRow][startColumn + 1] = pipes[startRow][startColumn + 1]
  startConnections.add('E')
if startRow != numRows - 1 and 'S' in pipeFlow[pipes[startRow + 1][startColumn]].keys():
  rowChange, columnChange, direction = pipeFlow[pipes[startRow + 1][startColumn]]['S']
  currentRow = startRow + 1 + rowChange
  currentColumn = startColumn + columnChange
  path[startRow + 1][startColumn] = pipes[startRow + 1][startColumn]
  startConnections.add('S')

S = ''
if 'N' in startConnections and 'S' in startConnections:
  S = '|'
elif 'N' in startConnections and 'W' in startConnections:
  S = 'J'
elif 'N' in startConnections and 'E' in startConnections:
  S = 'L'
elif 'S' in startConnections and 'W' in startConnections:
  S = '7'
elif 'S' in startConnections and 'E' in startConnections:
  S = 'F'
elif 'E' in startConnections and 'W' in startConnections:
  S = '-'

path[currentRow][currentColumn] = pipes[currentRow][currentColumn]

count = 2
while pipes[currentRow][currentColumn] != 'S':
  rowChange, columnChange, direction = pipeFlow[pipes[currentRow][currentColumn]][direction]
  currentRow += rowChange
  currentColumn += columnChange
  path[currentRow][currentColumn] = pipes[currentRow][currentColumn]
  count += 1

print(f'Part 1: {int(count/2)}')


# Part 2
path[startRow][startColumn] = S

magnifyPath = []
for i in range(numRows - 1):
  magnifyPath.append(path[i])
  magnifyPath.append('X' * numColumns)

magnifyPath.append(path[-1])

for i in range(len(magnifyPath)):
  row = magnifyPath[i]
  new_row = row[0]
  for j in range(1, len(row)):
    new_row += 'X' + row[j]
  magnifyPath[i] = [*new_row]

mRows = len(magnifyPath)
mColumns = len(magnifyPath[0])

for i in range(mColumns):
  if magnifyPath[0][i] == '.':
    magnifyPath[0][i] = '0'
  elif magnifyPath[0][i] == 'X':
    if magnifyPath[0][i - 1] not in ('-', 'F', 'L'):
      magnifyPath[0][i] = '0'
    else:
      magnifyPath[0][i] = '-'
  
  if magnifyPath[-1][i] == '.':
    magnifyPath[-1][i] = '0'
  elif magnifyPath[-1][i] == 'X':
    if magnifyPath[-1][i - 1] not in ('-', 'F', 'L'):
      magnifyPath[-1][i] = '0'
    else:
      magnifyPath[-1][i] = '-'

for i in range(1, mRows - 1):
  if magnifyPath[i][0] == '.':
    magnifyPath[i][0] = '0'
  elif magnifyPath[i][0] == 'X':
    if magnifyPath[i - 1][0] not in ('|', 'F', '7'):
      magnifyPath[i][0] = '0'
    else:
      magnifyPath[i][0] = '|'

  if magnifyPath[i][-1] == '.':
    magnifyPath[i][-1] = '0'
  elif magnifyPath[i][-1] == 'X':
    if magnifyPath[i - 1][-1] not in ('|', 'F', '7'):
      magnifyPath[i][-1] = '0'
    else:
      magnifyPath[i][-1] = '|'

for i in range(1, mRows - 1):
  if i % 2:
    for j in range(1, mColumns - 1):
      if magnifyPath[i - 1][j] in ('|', 'F', '7'):
        magnifyPath[i][j] = '|'
  else:
    for j in range(1, mColumns, 2):
      if magnifyPath[i][j - 1] in ('-', 'F', 'L'):
        magnifyPath[i][j] = '-'

tileRemoved = True
while tileRemoved:
   magnifyPath, tileRemoved = removeExterior(magnifyPath, mRows, mColumns)

interiorCount = 0
for row in magnifyPath:
  for tile in row:
    if tile == '.':
      interiorCount += 1

GREY = '\033[90m'
YELLOW = '\033[93m'
RED = '\033[91m'
GREEN = '\033[92m'
RESET_COLOR = '\033[0m'

for row in magnifyPath:
  rowString = ''
  for char in row:
    if char == '0':
      rowString += GREY + char + RESET_COLOR
    elif char == 'X':
      rowString += YELLOW + char + RESET_COLOR
    elif char == '.':
      rowString += RED + char + RESET_COLOR
    else:
      rowString += GREEN + char + RESET_COLOR

  print(rowString)
print(f'Part 2: {interiorCount}')