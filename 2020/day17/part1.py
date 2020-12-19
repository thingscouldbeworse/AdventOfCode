DIMENSION = 100

def print_slice(index, grid):
  for i in grid[index]:
    for j in i:
      print(j, end='')
    print()

def get_neighbors(z, y, x, grid):
  neighbors = 0
  for i in range(-1, 2):
    for j in range(-1, 2):
      for k in range(-1,2):
        try:
          if grid[z+i][y+j][x+k] == '#' and not (z+i == z and y+j == y and x+k == x):
            neighbors += 1
        except:
          pass
  return neighbors

def run_geration(grid):
  new_grid = [[['.' for i in range(DIMENSION)] for j in range(DIMENSION)] for k in range(DIMENSION)] 
  for z in range(0, len(grid)):
    for y in range(0, len(grid[z])):
      for x in range(0, len(grid[z][y])):
        num_neighbors = get_neighbors(z, y, x, grid)
        if grid[z][y][x] == '#':
          if num_neighbors < 2 or num_neighbors > 3:
            new_grid[z][y][x] = '.'
          else:
            new_grid[z][y][x] = '#'
        elif grid[z][y][x] == '.' and num_neighbors == 3:
          new_grid[z][y][x] = '#'
  return new_grid

# z, y, x
grid = [[['.' for i in range(DIMENSION)] for j in range(DIMENSION)] for k in range(DIMENSION)] 
z = int(DIMENSION/2)
with open("input.txt", 'r') as inputdata:
  y = int(DIMENSION/2)
  for line in inputdata:
    x = int(DIMENSION/2)
    for char in line[:-1]:
      x += 1
      grid[z][y][x] = char
    y += 1

for i in range(0,6):
  print("running gen " + str(i))
  grid = run_geration(grid)

x = 0
z = 0
count = 0
for i in grid:
  y = 0
  for j in i:
    x = 0
    for k in j:
      if k == "#":
        #neighbors = get_neighbors(z, y, x, grid)
        #print(str(y)+", "+str(x)+ ": " +str(neighbors))
        count += 1
      x += 1
    y += 1
  z += 1
print(count)

