data = []
import sys

with open ("input.txt") as inputdata:
  for line in inputdata:
    data.append(int(line[:-1]))

i = 25
upper_bound = len(data)
while i <= upper_bound-1:
  print(str(i)+"/"+str(upper_bound))
  preamble = data[i-25:]
  found = False
  for x in preamble:
    for y in preamble:
      if x != y and (x + y) == data[i]:
        #print("for " + str(data[i]) + " found the pair of " + str(x)+" and "+str(y))
        found = True
  if not found:
    print(data[i])
    sys.exit(1)
  i += 1
