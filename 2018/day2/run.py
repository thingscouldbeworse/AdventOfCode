with open('input.txt', 'r') as inputfile:
  twos = 0
  threes = 0
  for line in inputfile:
    sums = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    for letter in line[:-1]:
      sums[letter] += 1
    if 3 in sums.values():
      threes += 1
    if 2 in sums.values():
      twos += 1
  print("%s x %s = %s"%(twos,threes,twos*threes))
