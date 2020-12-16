def apply_bitmask(decimal_number, bitmask):
  binary_string = bin(decimal_number)
  bitmask_split = [x for x in bitmask]
  binary_string = str(binary_string)[2:]
  for i in range(0,36-len(binary_string)):
    binary_string = "0" + binary_string
  i = 0
  while i < len(binary_string):
    if bitmask_split[i] != '0':
      binary_string = binary_string[:i] + bitmask_split[i] + binary_string[i+1:]
    i += 1

  return binary_string

def get_all_addresses(decimal_number, bitmask):
  x_addr = apply_bitmask(decimal_number, bitmask)
  addresses = {x_addr}
  done = False
  while not done:
    new_addresses = set()
    for addr in addresses:
      for i in range(0, len(addr)):
        if addr[i] == "X":
          new_addresses.add(addr[:i] + "1" + addr[i+1:])
          new_addresses.add(addr[:i] + "0" + addr[i+1:])
    addresses = new_addresses
    done = True
    for addr in addresses:
      if "X" in addr:
        done = False
  return addresses
        

lines = []
with open("input.txt", 'r') as inputfile:
  for line in inputfile:
    lines.append(line[:-1])

banks = {}
mask = ''
for line in lines:
  if line[:4] == "mask":
    mask = line.split(" ")[-1]
  else:
    value = int(line.split(" ")[-1])
    address = int(line.split("[")[1].split("]")[0])
    addresses = get_all_addresses(address, mask)
    for addr in addresses:
      banks[int(addr, 2)] = value

total_sum = 0
for addr in banks:
  total_sum += banks[addr]
print(total_sum)
