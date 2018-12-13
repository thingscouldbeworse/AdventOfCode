with open('input.txt', 'r') as inputfile:
  data = []
  for line in inputfile:
    data.append(line[:-1])

found1 = ''
found2 = ''
least = 100
for line in data:
  print(line)
  for line2 in data:
    num_off = 0 
    print("\t"+line2)
    for i in range(0,len(line)):
      if line[i] != line2[i]:
        num_off += 1
    if num_off < least and num_off != 0:
      found1 = line
      found2 = line2
      least = num_off

print(least)
print(found1)
print(found2)

new = ''
for i in range(0,len(found2)):
  if found1[i] == found2[i]:
    new += found1[i]
print(new)
