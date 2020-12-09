import sys
data = []

with open('input1.txt', 'r') as raw_input:
  for line in raw_input:
    data.append(int(line))

for item in data:
  for item2 in data:
    for item3 in data:
      if (item + item2 + item3) == 2020:
        print(str(item) + " " + str(item2) + " " + str(item3))
        print(item * item2 * item3)
        sys.exit(1)
