DIMENSION = 30

def get_neighbors(w, z, y, x, grid):
  neighbors = 0
  for i in range(-1, 2):
    for j in range(-1, 2):
      for k in range(-1, 2):
        for l in range(-1, 2):
          try:
            if grid[w+i][z+j][y+k][x+l] == '#' and not (w+i == w and z+j == z and y+k == y and x+l == x):
              neighbors += 1
          except:
            pass
  return neighbors

def run_geration(grid):
  new_grid = [[[['.' for i in range(DIMENSION)] for j in range(DIMENSION)] for k in range(DIMENSION)] for l in range(DIMENSION)]
  for w in range(0, len(grid)):
    for z in range(0, len(grid[w])):
      for y in range(0, len(grid[w][z])):
        for x in range(0, len(grid[w][z][y])):
          num_neighbors = get_neighbors(w, z, y, x, grid)
          if grid[w][z][y][x] == '#':
            if num_neighbors < 2 or num_neighbors > 3:
              new_grid[w][z][y][x] = '.'
            else:
              new_grid[w][z][y][x] = '#'
          elif grid[w][z][y][x] == '.' and num_neighbors == 3:
            new_grid[w][z][y][x] = '#'
  return new_grid

# w, z, y, x
grid = [[[['.' for i in range(DIMENSION)] for j in range(DIMENSION)] for k in range(DIMENSION)] for l in range(DIMENSION)]
w = int(DIMENSION/2)
z = int(DIMENSION/2)
with open("input.txt", 'r') as inputdata:
  y = int(DIMENSION/2)
  for line in inputdata:
    x = int(DIMENSION/2)
    for char in line[:-1]:
      x += 1
      grid[w][z][y][x] = char
    y += 1

for i in range(0,6):
  print("running gen " + str(i))
  grid = run_geration(grid)

w = 0
x = 0

count = 0
for l in grid:
  z = 0
  for i in l:
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
  w += 1
print(count)

