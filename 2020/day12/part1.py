directions = []
next_orientation = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
next_orientation_L = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}

def increment(x, y, direction, magnitude): 
  if direction == "E":
    x = x + magnitude
  elif direction == "N":
    y = y + magnitude
  elif direction == "W":
    x = x - magnitude
  elif direction == "S":
    y = y - magnitude
  return x, y

x = 0
y = 0
with open('input.txt', 'r') as data:
  orientation = 'E'
  for line in data:
    direction = line[0]
    magnitude = int(line[1:-1])
    if direction == "R":
      for i in range(0, int(magnitude/90)):
        orientation = next_orientation[orientation]
    elif direction == "L":
      for i in range(0, int(magnitude/90)):
        orientation = next_orientation_L[orientation]
    elif direction == "F":
      x, y = increment(x, y, orientation, magnitude)
    else:
      x, y = increment(x, y, direction, magnitude)
  
print()
print(x)
print(y)
print(abs(x) + abs(y))
