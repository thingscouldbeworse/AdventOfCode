class bag:

    def __init__(self, data):
      self.bags = []
      self.color = data
      self.unique_colors = set()

    def pretty_print(self):
      print(self.color + " bag with " + str(len(self.bags)) + " bags of")
      for item in self.bags:
        print(item.color)

class counter:

  def __init__(self):
    self.count = 0

def find_bag_inner(color_to_find, bags):
  for line in bags:
    if color_to_find in line:
      outer_color = line.split("bags")[0][:-1]
      if outer_color == color_to_find:
        found_bag = bag(color_to_find)
        inners = line.split("contain")[1].split(",")
        for item in inners:
          if item.split(" ")[1] == "no":
            num_bags = 0
          else:
            num_bags = int(item.split(" ")[1])
            color = " ".join(item.split(" ")[2:-1])
            found_bag.unique_colors.add(color)
            for i in range(0,num_bags):
              inner_bag = bag(color)
              found_bag.bags.append(inner_bag)
        
        return found_bag  

def recurse(start_bag, bags):
  for bag_item in start_bag.bags:
    new_bag = find_bag_inner(bag_item.color, bags)
    bag_item.bags.append(new_bag)
    recurse(new_bag, bags)
  our_count.count += 1

  
bags = []
with open("input.txt") as data:
  for line in data:
    bags.append(line[:-1])

in_bag = find_bag_inner("shiny gold", bags)
our_count = counter()
our_count.count = 1
recurse(in_bag, bags)
print(our_count.count - 2)
