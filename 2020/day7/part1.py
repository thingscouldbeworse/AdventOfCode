def find_bag_outer(color_to_find, bags):
  outer_colors = []
  for line in bags:
    if color_to_find in line:
      outer_color = line.split("bags")[0][:-1]
      if outer_color != color_to_find:
        outer_colors.append(outer_color)

  return outer_colors

def recurse(list_of_colors, bags, bags_that_can_contain):
  print(list_of_colors)
  for color in list_of_colors:
    bags_that_can_contain.setdefault(color, '')
  for color in list_of_colors:
    colors = find_bag_outer(color, bags)
    recurse(colors, bags, bags_that_can_contain)

bags = []
with open("input.txt") as data:
  for line in data:
    bags.append(line[:-1])

bags_that_can_contain = {}
outers = find_bag_outer("shiny gold", bags)
for color in outers:
  bags_that_can_contain.setdefault(color, '')
recurse(outers, bags, bags_that_can_contain)
print(bags_that_can_contain)
print(len(bags_that_can_contain))
