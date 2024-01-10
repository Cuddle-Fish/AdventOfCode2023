FILENAME = 'data/day09.txt'

# Part 1 and 2
part1Sum = 0
part2Sum = 0
with open(FILENAME) as f:
  for line in f:
    firstDiff = []
    lastDiff = []
    nums = [int(num) for num in line.rstrip().split()]
    length = len(nums)
    firstDiff.append(nums[0])
    sign = 1
    while True:
      sign *= -1
      allZero = True
      for i in range(length - 1):
        nums[i] = nums[i + 1] - nums[i]
        if nums[i] != 0:
          allZero = False
      length -= 1
      lastDiff.append(nums[length])
      firstDiff.append(nums[0] * sign)
      if allZero:
        break
    part1Sum += sum(lastDiff)
    part2Sum += sum(firstDiff)
print(f'Part 1: {part1Sum}')
print(f'Part 2: {part2Sum}')