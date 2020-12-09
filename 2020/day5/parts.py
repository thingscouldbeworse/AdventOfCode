import math

def find_row(first_7):
  whole_range = list(range(0,128))
  for char in first_7:
    if char == 'F':
      whole_range = whole_range[:len(whole_range)//2]
    elif char == 'B':
      whole_range = whole_range[math.ceil(len(whole_range)/2):]
  
  return whole_range[0]

def find_column(last_3):
  whole_range = list(range(0,8))
  for char in last_3:
    if char == 'L':
      whole_range = whole_range[:len(whole_range)//2]
    elif char == 'R':
      whole_range = whole_range[math.ceil(len(whole_range)/2):]
  
  return whole_range[0]

def find_highest_seat_id():
  highest = 0
  with open('input.txt', 'r') as data:
    for line in data:
      first_7 = line[:8]
      last_3 = line[7:-1]
      row = find_row(first_7)
      column = find_column(last_3)
      seat_id = (row * 8) + column
      if seat_id > highest:
        highest = seat_id
  print(highest)

def find_missing_seats():
  grid = [['X' for i in range(8)] for j in range(127)]
  with open('input.txt', 'r') as data:
    for line in data:
      first_7 = line[:8]
      last_3 = line[7:-1]
      row = find_row(first_7)
      column = find_column(last_3)
      grid[row][column] = '0'
  
  i = 0
  for line in grid:
    print(str(i) + str(line))
    i += 1
      

find_missing_seats()
print((80*8)+2)