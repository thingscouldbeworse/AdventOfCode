snow_map = []
with open("input.txt", 'r') as inputdata:
  for line in inputdata:
    snow_map.append(line[:-1])
  
bottom_bound = len(snow_map)
right_bound = len(snow_map[0])
x_pos = 0
y_pos = 0

tree_count = 0
for i in range(0, bottom_bound+2, 2):
  if i >= bottom_bound:
    break
  else:
    y_pos = i
  if x_pos >= right_bound:
    x_pos = x_pos - right_bound
  if snow_map[y_pos][x_pos] == '#':
    tree_count += 1
  print(snow_map[y_pos][:x_pos] + "X" + snow_map[y_pos][x_pos+1:])
  print(tree_count)
  x_pos += 1
