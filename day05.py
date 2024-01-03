FILENAME = "data/day05.txt"
# FILENAME = 'test.txt'

class conversionVals:
  def __init__(self, dest, src, range):
    self.dest = dest
    self.src = src
    self.range = range

  def inRange(self, num):
    if num >= self.src and num < self.src + self.range:
      return True
    else:
      return False
  
  def convertValue(self, num):
    diff = self.src - self.dest
    return num - diff
  
  def lowerRange(self, rangeReduction):
    self.dest += rangeReduction
    self.src += rangeReduction
    self.range -= rangeReduction

  def copy(self):
    return conversionVals(self.dest, self.src, self.range)
  
  def __str__(self):
    return f'[{self.dest}, {self.src}, {self.range}]'

def extractInfo(section):
  map = []
  _, catagory = section.pop(0).split("-to-")
  catagory = catagory.rstrip(" map:")

  while section:
    nums = [int(num) for num in section.pop(0).split()]
    values = conversionVals(nums[0], nums[1], nums[2])
    map.append(values)
  return catagory, map

def printMap(catagory, map):
  print(f'{catagory} map:')
  item = 1
  for conversion in map:
    print(f'  {item}: {conversion}')
    item += 1

def getConversion(map, num):
  for conversion in map:
    if conversion.inRange(num):
      return conversion.convertValue(num)
  return num

def getLowestLocation(chart):
  return min(chart, key=lambda x: x['location'])['location']


# Part 1
with open(FILENAME) as f:
  seedString = f.readline().rstrip().strip("seeds: ")
  seeds = [int(seed) for seed in seedString.split()]
  
  conversionChart = []
  for seed in seeds:
    conversionChart.append({'seed': seed})

  # print(conversionChart)
  previousCatagory = 'seed'
  f.readline()

  map = []
  section = []
  for line in f:
    content = line.rstrip()
    if content:
      section.append(content)
    else:
      catagory, map = extractInfo(section)

      # printMap(catagory, map)

      for seed in conversionChart:
        newValue = getConversion(map, seed[previousCatagory])
        seed[catagory] = newValue

      previousCatagory = catagory
      map = []
  
  catagory, map = extractInfo(section)
  # printMap(catagory, map)

  for seed in conversionChart:
    newValue = getConversion(map, seed[previousCatagory])
    seed[catagory] = newValue
  
  # for conversion in conversionChart:
  #   print(conversion)

  print(f'Part 1: {getLowestLocation(conversionChart)}')


# Part 2
def sortMapByDest(map):
  return sorted(map, key=lambda x:x.dest)

def sortMapBySrc(map):
  return sorted(map, key=lambda x:x.src)

def combineMaps(base, next):
  base = sortMapByDest(base)
  next = sortMapBySrc(next)
  newMap = []
  baseLen = len(base)
  baseIndex = 0
  currentBase = base[baseIndex]
  for section in next:
    if (baseIndex >= baseLen):
      newMap.append(section)
    else:
      while section.range > 0 and baseIndex < baseLen:
        while currentBase.dest < section.src:
          if (currentBase.dest + currentBase.range - 1) < section.src:
            newMap.append(currentBase.copy())
            baseIndex += 1
            if (baseIndex >= baseLen):
              break
            currentBase = base[baseIndex]
          else:
            difference = section.src - currentBase.dest
            newSection = conversionVals(currentBase.dest, currentBase.src, difference)
            newMap.append(newSection)
            currentBase.lowerRange(difference)

        if (baseIndex >= baseLen):
          break

        if section.src < currentBase.dest:
          if (section.src + section.range - 1) < currentBase.dest:
            newMap.append(section.copy())
            section.range = 0
          else:
            difference = currentBase.dest - section.src
            newSection = conversionVals(section.dest, section.src, difference)
            newMap.append(newSection)
            section.lowerRange(difference)

        if section.src == currentBase.dest:
          if section.range < currentBase.range:
            section.src = currentBase.src
            newMap.append(section.copy())
            currentBase.lowerRange(section.range)
            section.range = 0
          else:
            currentBase.dest = section.dest
            newMap.append(currentBase.copy())
            section.lowerRange(currentBase.range)
            baseIndex += 1
            if (baseIndex < baseLen):
              currentBase = base[baseIndex]

  while baseIndex < baseLen:
    newMap.append(currentBase.copy())
    baseIndex += 1
    if baseIndex < baseLen:
      currentBase = base[baseIndex]

  return newMap

with open(FILENAME) as f:
  seedString = f.readline().rstrip().strip("seeds: ")
  seedNums = [int(seed) for seed in seedString.split()]
  seeds = [seedNums[i:i+2] for i in range(0, len(seedNums), 2)]
  seeds = sorted(seeds, key=lambda x:x[0])
  # print(f'seed groups: {seeds}')

  seedToLocationMap = []
  f.readline()
  for line in f:
    content = line.rstrip()
    if content:
      section.append(content)
    else:
      break
  catagory, seedToLocationMap = extractInfo(section)
  
  # printMap(catagory, seedToLocationMap)
  currentMap = []

  section = []
  for line in f:
    content = line.rstrip()
    if content:
      section.append(content)
    else:
      catagory, map = extractInfo(section)
      seedToLocationMap = combineMaps(seedToLocationMap, map)
      # printMap(catagory, seedToLocationMap)
  
  catagory, map = extractInfo(section)
  seedToLocationMap = combineMaps(seedToLocationMap, map)

  seedToLocationMap = sortMapBySrc(seedToLocationMap)
  # printMap('seed-to-location', seedToLocationMap)

  mapLen = len(seedToLocationMap)
  lowestLocation = seeds[0][0]
  mapIndex = 0
  for group in seeds:
    groupStart = group[0]
    groupEnd = group[0] + group[1] - 1

    while mapIndex < mapLen:
      if seedToLocationMap[mapIndex].src > groupEnd:
        break
      if groupStart > (seedToLocationMap[mapIndex].src + seedToLocationMap[mapIndex].range - 1):
        mapIndex += 1
      else:
        if groupStart < seedToLocationMap[mapIndex].src:
          if seedToLocationMap[mapIndex].dest < lowestLocation:
            lowestLocation = seedToLocationMap[mapIndex].dest
          mapIndex += 1
        else:
          conversion = seedToLocationMap[mapIndex].convertValue(groupStart)
          if conversion < lowestLocation:
            lowestLocation = conversion
          mapIndex += 1

  print(f'Part 2: {lowestLocation}')