data = []

with open("input.txt", 'r') as datafile:
  i = 0
  for line in datafile:
    if i < 1:
      timestamp = int(line[:-1])
      i += 1
    else:
      ids = line[:-1].split(",")

i = 0
earliest = timestamp * 2
early_id = 0
while i < len(ids):
  if ids[i] != 'x':
    int_id = int(ids[i])
    remainder = timestamp % int_id
    if(remainder == 0):
      print("bus " + str(int_id))
    else:
      potential = timestamp - remainder + int_id
      if potential < earliest:
        earliest = potential
        early_id = int_id
  i += 1

print("bus " + str(early_id))
print("Will wait " + str(earliest - timestamp))
print(early_id * (earliest - timestamp))
