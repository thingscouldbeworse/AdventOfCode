groups = []
with open("input.txt", 'r') as data:
  group = {}
  lines = 0
  for line in data:
    if line == "\n":
      group["lines"] = lines
      groups.append(group)
      group = {}
      lines = 0
    else:
      lines += 1
      for char in line[:-1]:
        if char not in group:
          group[char] = 1
        elif char in group:
          group[char] += 1

total_count = 0  
for group in groups:
  print(group)
  for key in group:
    if group[key] == group["lines"] and key != "lines":
      total_count += 1
  print(total_count)

print(total_count)
