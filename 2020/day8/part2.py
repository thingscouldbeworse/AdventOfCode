
def will_loop(instructions):
  accumulator = 0
  i = 0
  line_numbers = set()
  while i <= len(instructions):
    if i >= len(instructions) - 1:
      return False, accumulator
    if i in line_numbers:
      return True, accumulator
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


instructions = []

with open("input.txt", 'r') as data:
  for line in data:
    instructions.append(line[:-1])

instruction_copy = instructions.copy()

j = 0
while j <= len(instructions):
  instructions = instruction_copy.copy()
  instruction = instructions[j].split(" ")[0]
  looping = True
  acc = 0
  if instruction == "nop":
    instructions[j] = "jmp " + instructions[j].split(" ")[1] 
    looping, acc = will_loop(instructions)
  elif instruction == "jmp":
    instructions[j] = "nop " + instructions[j].split(" ")[1]
    looping, acc = will_loop(instructions)
  if not looping:
    print(acc)
    break
  j += 1
  
    


