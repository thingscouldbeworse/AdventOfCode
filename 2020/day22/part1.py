decks = {}
player_index = 0
with open("input.txt", 'r') as inputfile:
  for line in inputfile:
    if "Player" in line:
      player_index = int(line[-3])
    elif line != "\n":
      try:
        decks[player_index].append(int(line[:-1]))
      except:
        decks[player_index] = [int(line[:-1])]

count = 0
while len(decks[1]) > 0 and len(decks[2]) > 0:
  print(decks)
  num1 = decks[1][0]
  num2 = decks[2][0]
  if num1 > num2:
    del decks[1][0]
    del decks[2][0]
    try:
      decks[1].append(num1)
      decks[1].append(num2)
    except:
      pass
  else:
    del decks[1][0]
    del decks[2][0]
    try:
      decks[2].append(num2)
      decks[2].append(num1)
    except:
      pass
  count += 1

score = 0
winning_deck = decks[1][-1::-1]
for i in range(1, len(winning_deck) + 1):
  score += i * winning_deck[i-1]
print(score)
