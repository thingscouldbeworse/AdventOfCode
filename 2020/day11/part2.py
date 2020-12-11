import collections

def is_occupied(x, y, grid):
  if x > -1 and x < len(grid[0]) and y > -1 and y < len(grid):
    if grid[y][x] == '#':
      return "Occupied"
    elif grid[y][x] == 'L':
      return "Open"
    else:
      return "Floor"

def test_lines(x, y, grid):
  num_occupied = 0
  left_up_found = False
  right_up_found = False
  right_down_found = False
  left_down_found = False
  left_found = False
  up_found = False
  right_found = False
  down_found = False

  # left
  for test_x in range(x-1, -1, -1):
    if not left_found:
      occupied = is_occupied(test_x, y, grid)
      if occupied == "Occupied":
        num_occupied += 1
        left_found = True 
      elif occupied == "Open":
        left_found = True
  # up
  for test_y in range(y-1, -1, -1):
    if not up_found:
      occupied = is_occupied(x, test_y, grid)
      if occupied == "Occupied":
        num_occupied += 1
        up_found = True
      elif occupied == "Open":
        up_found = True
  # down
  for test_y in range(y+1, len(grid)+1, 1):
    if not down_found:
      occupied = is_occupied(x, test_y, grid)
      if occupied == "Occupied":
        num_occupied += 1
        down_found = True
      elif occupied == "Open":
        down_found = True
  # right
  for test_x in range(x+1, len(grid[0])+1, 1):
    if not right_found:
      occupied = is_occupied(test_x, y, grid)
      if occupied == "Occupied":
        num_occupied += 1
        right_found = True
      elif occupied == "Open":
        right_found = True

  for i in range(1, len(grid)+1):
    # left + up
    if not left_up_found:
      test_x = x - i
      test_y = y - i
      occupied = is_occupied(test_x, test_y, grid)
      if occupied == "Occupied":
        num_occupied += 1
        left_up_found = True
      elif occupied == "Open":
        left_up_found = True
    # right + up
    if not right_up_found:
      test_x = x + i
      test_y = y - i
      occupied = is_occupied(test_x, test_y, grid)
      if occupied == "Occupied":
        num_occupied += 1
        right_up_found = True
      elif occupied == "Open":
        right_up_found = True
    # right + down
    if not right_down_found:
      test_x = x + i
      test_y = y + i
      occupied = is_occupied(test_x, test_y, grid)
      if occupied == "Occupied":
        num_occupied += 1
        right_down_found = True
      elif occupied == "Open":
        right_down_found = True
    # left + down
    if not left_down_found:
      test_x = x - i
      test_y = y + i
      occupied = is_occupied(test_x, test_y, grid)
      if occupied == "Occupied":
        num_occupied += 1
        left_down_found = True
      elif occupied == "Open":
        left_down_found = True

  return num_occupied

def run_generation(grid):
  grid_new = grid.copy()
  for j in range(0, len(grid)):
    for i in range(0, len(grid[j])):
      num_occupied = test_lines(i, j, grid)
      if grid[j][i] == "L" and num_occupied == 0:
        grid_new[j] = grid_new[j][:i] + "#" + grid_new[j][i+1:]
      elif grid[j][i] == "#" and num_occupied >= 5:
        grid_new[j] = grid_new[j][:i] + "L" + grid_new[j][i+1:]

  return grid_new
  
def iterate(grid):
  done = False
  gen_counter = 1
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
#print(test_lines(2, 2, grid))
