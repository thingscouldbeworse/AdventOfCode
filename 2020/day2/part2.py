from operator import xor
count_pass = 0
with open("input.txt", 'r') as inputdata:
  for line in inputdata:
    line_split = line.split(":")
    letter = line_split[0][-1]
    position1 = int(line_split[0].split("-")[0])
    position2 = int(line_split[0].split("-")[1][:-2])
    if xor(bool(line_split[1][position1] == letter), bool(line_split[1][position2] == letter)):
      count_pass += 1
print(count_pass)
