import sys

def sum_all(sum_list):
  total = 0
  for num in sum_list:
    total += num
  return total

data = []
NUM_TO_FIND = 29221323
#NUM_TO_FIND = 127

with open ("input.txt") as inputdata:
  for line in inputdata:
    data.append(int(line[:-1]))

summation = []
count = 0
i = 0
while i <= len(data)-1:
  summation.append(data[i])
  if sum_all(summation) == NUM_TO_FIND:
    print(summation)
    print(min(summation) + max(summation))
    sys.exit(1)
  i += 1
  if i == len(data):
    summation = []
    count += 1
    i = count