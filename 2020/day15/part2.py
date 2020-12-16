numbers = []
indices = {}

i = 0
with open("input.txt", 'r') as inputfile:
  for line in inputfile:
    numbers.append(int(line[:-1]))
    indices[int(line[:-1])] = [i]
    i += 1

last_num = numbers[-1]
for i in range(len(numbers)-1, 30000000 - 1):
  if len(indices[last_num]) == 1:
    last_num = 0
    indices[0].append(i + 1)
  else:
    difference = indices[last_num][-1] - indices[last_num][-2]
    last_num = difference
    if difference in indices:
      indices[difference].append(i + 1)
    else:
      indices[difference] = [i + 1]
      
print(last_num)
