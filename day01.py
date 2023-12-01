lines = []
with open("data/day01.txt") as f:
  lines = f.readlines()

sum = 0

# Part 1
for string in lines:
  length = len(string)
  index = 0
  first = 0
  last = 0
  for i in range(index, length):
    if (string[i].isnumeric()):
        first = int(string[i])
        break
    index += 1
  for i in range(index, length):
    if (string[i].isnumeric()):
        last = int(string[i])
  sum += (first * 10) + last

print(sum)

# Part 2
sum = 0
numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for string in lines:
  length = len(string)
  stringNums = []
  for index in range(0, length):
    if string[index].isnumeric():
      stringNums.append(int(string[index]))
    else:
      for num in range(0, 9):
        if string.startswith(numbers[num], index):
          stringNums.append(num + 1)
          break
  sum += (stringNums[0] * 10) + stringNums[len(stringNums) - 1]

print(sum)