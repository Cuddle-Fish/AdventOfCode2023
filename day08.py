from math import lcm

FILENAME = 'data/day08.txt'

instructions = ''
map = {}
positions = []
with open(FILENAME) as f:
  instructions = f.readline().rstrip()
  f.readline()

  for line in f:
    source, elements = line.rstrip().split(' = ')
    if source[2] == 'A':
      positions.append(source)
    elements = elements[1:-1]
    elements = elements.split(', ')
    map[source] = elements


# Part 1
position = 'AAA'
count = 0
while position != 'ZZZ':
  for instruction in instructions:
    position = map[position][0] if instruction == 'L' else map[position][1]
    count += 1
    if position == 'ZZZ':
      break

print(f'Part 1: {count}')


# Part 2
steps = []
for position in positions:
  count = 0
  while position[2] != 'Z':
    for instruction in instructions:
      position = map[position][0] if instruction == 'L' else map[position][1]
      count += 1
      if position[2] == 'Z':
        break
  steps.append(count)

print(f'Part 2: {lcm(*steps)}')