instructions = []

with open("input.txt", 'r') as data:
  for line in data:
    instructions.append(line[:-1])

accumulator = 0
i = 0
line_numbers = set()

while i <= len(instructions):
  if i in line_numbers:
    print(accumulator)
    break
  else:
    line_numbers.add(i)
  instruction = instructions[i].split(" ")[0]
  arg = int(instructions[i].split(" ")[1])
  if instruction == "acc":
    accumulator += arg
    i += 1
  elif instruction == "jmp":
    i += arg
  else:
    i += 1
