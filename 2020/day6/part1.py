groups = []
with open("input.txt", 'r') as data:
  group = {}
  for line in data:
    if line == "\n":
      groups.append(group)
      group = {}
    else:
      for char in line[:-1]:
        group.setdefault(char,"1")

total_count = 0
for group in groups:
  total_count += len(group)

print(total_count)
