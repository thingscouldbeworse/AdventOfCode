def apply_bitmask(decimal_number, bitmask):
  binary_string = bin(decimal_number)
  bitmask_split = [x for x in bitmask]
  binary_string = str(binary_string)[2:]
  for i in range(0,36-len(binary_string)):
    binary_string = "0" + binary_string
  i = 0
  while i < len(binary_string):
    if bitmask_split[i] != 'X':
      binary_string = binary_string[:i] + bitmask_split[i] + binary_string[i+1:]
    i += 1

  return binary_string

lines = []
with open("input.txt", 'r') as inputfile:
  for line in inputfile:
    lines.append(line[:-1])

memory_banks = {}
for line in lines:
  if line[:4] == "mask":
    mask = line.split(" ")[-1]
  else:
    bank_id = int(line.split("[")[1].split("]")[0])
    num = int(line.split(" ")[-1])
    memory_banks[bank_id] = int(apply_bitmask(num, mask), 2)

print(memory_banks)
summation = 0
for id in memory_banks:
  summation += memory_banks[id]

print(summation)
