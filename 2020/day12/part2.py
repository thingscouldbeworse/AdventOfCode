directions = []

def increment(x, y, direction, magnitude):
  print("moving waypoint") 
  if direction == "E":
    x = x + magnitude
  elif direction == "N":
    y = y + magnitude
  elif direction == "W":
    x = x - magnitude
  elif direction == "S":
    y = y - magnitude
  return x, y

def increment_with_wp(x, y, wp_x, wp_y, magnitude):
  print("moving forward " + str(magnitude))
  x = x + (magnitude * wp_x)
  y = y + (magnitude * wp_y)
  return x, y

def rotate(x, y, swap_x, swap_y):
  new_y = swap_x * x
  new_x = swap_y * y
  return new_x, new_y


x = 0
y = 0

wp_x = 10
wp_y = 1

with open('test.txt', 'r') as data:
  for line in data:
    print(line[:-1])
    direction = line[0]
    magnitude = int(line[1:-1])
    if direction == "R":
      for i in range(0, int(magnitude/90)):
        wp_x, wp_y = rotate(wp_x, wp_y, -1, 1)
    elif direction == "L":
      for i in range(0, int(magnitude/90)):
        wp_x, wp_y = rotate(wp_x, wp_y, 1, -1)
    elif direction == "F":
      x, y = increment_with_wp(x, y, wp_x, wp_y, magnitude)
    else:
      wp_x, wp_y = increment(wp_x, wp_y, direction, magnitude)
  
print()
print(x)
print(y)
print(abs(x) + abs(y))
