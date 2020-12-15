data = []
with open("input.txt", "r") as inputdata:
  data.insert(0,0)
  for line in inputdata:
    data.append(int(line[:-1]))

data = sorted(data)
data.append(data[-1] + 3)
print(data)

i = 1
node_count = 0
possibilities = 1
while i <= len(data) - 2:
  if data[i+1] - data[i-1] <= 3:
    node_count += 1
  else:
    if node_count == 3:
      possibilities = possibilities * 7
    elif node_count > 0:
      possibilities = possibilities * (2 * node_count)
    node_count = 0
  
  i += 1
  
print(possibilities)
