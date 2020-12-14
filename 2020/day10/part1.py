chargers = []

with open ("input.txt", 'r') as data:
  for line in data:
    chargers.append(int(line[:-1]))
chargers = sorted(chargers)

differences = {}
for i in range(1, len(chargers)):
  difference = chargers[i] - chargers[i-1]
  if difference in differences:
    differences[difference] += 1
  else:
    differences.setdefault(difference, 1)

# to PC
differences[3] += 1
# from wall
differences[1] += 1
print(differences)
