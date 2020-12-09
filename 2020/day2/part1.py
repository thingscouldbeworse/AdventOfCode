count_pass = 0
with open("input.txt", 'r') as inputdata:
  for line in inputdata:
    line_split = line.split(":")
    letter = line_split[0][-1]
    minimum = int(line_split[0].split("-")[0])
    maximum = int(line_split[0].split("-")[1][:-2])
    letter_count = 0
    for letter_compare in line_split[1]:
      if letter_compare == letter:
        letter_count += 1
    if letter_count <= maximum and letter_count >= minimum:
      count_pass += 1
print(count_pass)
