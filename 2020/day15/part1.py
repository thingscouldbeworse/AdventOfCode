numbers = []
with open("input.txt", 'r') as inputfile:
  for line in inputfile:
    numbers.append(int(line[:-1]))

for i in range(len(numbers)-1, 2019):
  if numbers[i] not in numbers[:-1]:
    numbers.append(0)
  else:
    indices = [x for x, y in enumerate(numbers) if y == numbers[i]]
    numbers.append((indices[-1] + 1) - (indices[-2] + 1))
    

print(numbers)
