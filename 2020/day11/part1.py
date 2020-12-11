import collections

def is_occupied(x, y, grid):
  if x > -1 and x < len(grid[0]) and y > -1 and y < len(grid):
    if grid[y][x] == '#':
      return True

def test_adjacents(x, y, grid):
  num_occupied = 0
  for test_x in range(x-1,x+2):
    for test_y in range(y-1,y+2):
      if not (test_x == x and test_y == y) and is_occupied(test_x, test_y, grid):
        num_occupied += 1

  return num_occupied

def run_generation(grid):
  grid_new = grid.copy()
  for j in range(0, len(grid)):
    for i in range(0, len(grid[j])):
      num_occupied = test_adjacents(i, j, grid)
      if grid[j][i] == "L" and num_occupied == 0:
        grid_new[j] = grid_new[j][:i] + "#" + grid_new[j][i+1:]
      elif grid[j][i] == "#" and num_occupied >= 4:
        grid_new[j] = grid_new[j][:i] + "L" + grid_new[j][i+1:]
  
  return grid_new

def iterate(grid):
  done = False
  gen_counter = 0
  while not done:
    print()
    print("generation " + str(gen_counter))
    for line in grid:
      print(line)
    new_grid = run_generation(grid)
    if collections.Counter(new_grid) == collections.Counter(grid):
      done = True
      total_occupied = 0
      for y in range(0,len(grid)):
        for x in range(0, len(grid[0])):
          if grid[y][x] == "#":
            total_occupied += 1
      print("total occupied: " + str(total_occupied))
    else:
      grid = new_grid
    gen_counter += 1


grid = []
with open("input.txt", 'r') as data:
  for line in data:
    grid.append(line[:-1])

iterate(grid)
