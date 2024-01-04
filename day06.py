import math

FILENAME = 'data/day06.txt'

class race:
  def __init__(self, time, record):
    self.time = time
    self.record = record
  
  def getRangetoBeat(self):
    x = math.sqrt(self.time**2 - (4*self.record))
    timeToBeat01 = (-self.time + x) / -2
    timeToBeat02 = (-self.time - x) / -2
    if timeToBeat01.is_integer():
      timeToBeat01 += 1
    if timeToBeat02.is_integer():
      timeToBeat02 -= 1
    return math.ceil(timeToBeat01), math.floor(timeToBeat02)
  
  def __str__(self) -> str:
    return f'Time: {self.time},\tRecord: {self.record}'


# Part 1
nums = []
with open(FILENAME) as f:
  for line in f:
    _, values = line.split(':', 1)
    nums.append([int(num) for num in values.split()])

races = []
for i in range(0, len(nums[0])):
  races.append(race(nums[0][i], nums[1][i]))

waysToBeat = 1
for currentRace in races:
  start, end = currentRace.getRangetoBeat()
  waysToBeat *= end - start + 1
print(f'Part 1: {waysToBeat}')


# Part 2
time = int(''.join(map(str, nums[0])))
record = int(''.join(map(str, nums[1])))
actualRace = race(time, record)
start, end = actualRace.getRangetoBeat()
waysToBeat = end - start + 1
print(f'Part 2: {waysToBeat}')