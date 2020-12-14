import math

data = []
with open("test.txt", "r") as inputdata:
  data.insert(0,0)
  for line in inputdata:
    data.append(int(line[:-1]))

data = sorted(data)
data.append(data[-1] + 3)
print(data)

i = 1
nodes = []
num_alt_nodes = 0
while i <= len(data) - 2:
  if i + 1 < len(data) and (data[i+1] - data[i-1] <= 3):
    node = [data[i]] 
    if i + 2 < len(data) and data[i+2] - data[i-1] <= 3:
      num_alt_nodes += 1
      node.append(data[i+1])
      i += 1
    nodes.append(node)
  i += 1
  
  
print(nodes)
print(len(nodes))
print(num_alt_nodes)

#paths = int(math.pow(2, num_pure_nodes)) + num_duo_nodes + (num_duo_nodes * num_pure_nodes) + 1
#print(paths)
