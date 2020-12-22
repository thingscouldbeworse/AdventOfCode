from types import coroutine

def count_incidences(number, search_list):
  count = 0
  for item in search_list:
    if item == number:
      count += 1
  return count

rules = {}
tickets = []
write_tickets = False

with open("input.txt", 'r') as inputfile:
  for line in inputfile:
    if write_tickets:
      tickets.append(line[:-1].split(","))
    if "or" in line:
      name = line.split(":")[0]
      ranges = line[:-1].split(" ")
      rules[name] =  [ranges[1], ranges[3]]
    if "nearby tickets" in line:
      write_tickets = True

rule_to_index = {}
count_invalid = 0
sum_invalid = 0
for ticket in tickets:
  index = 0
  ticket_valid = True
  valid_rules = {}
  for number in ticket:
    number = int(number)
    valid = False
    for rule in rules:
      lower_bound_1 = int(rules[rule][0].split("-")[0])
      upper_bound_1 = int(rules[rule][0].split("-")[1])
      lower_bound_2 = int(rules[rule][1].split("-")[0])
      upper_bound_2 = int(rules[rule][1].split("-")[1])
      if (number >= lower_bound_1 and number <= upper_bound_1) or (number >= lower_bound_2 and number <= upper_bound_2):
        valid = True
        try:
          valid_rules[rule].append(index)
        except:
          valid_rules[rule] = [index]
    if not valid:
      count_invalid += 1
      sum_invalid += number
      ticket_valid = False
    index += 1
  if ticket_valid:
    for rule in valid_rules:
      try:
        rule_to_index[rule] = rule_to_index[rule] + (valid_rules[rule])
      except:
        if len(valid_rules[rule]) > 1:
          rule_to_index[rule] = valid_rules[rule]
        else:
          rule_to_index[rule] = [valid_rules[rule]]

possibles = {}
num_valid_tickets = len(tickets) - count_invalid
for rule in rule_to_index:
  for i in range(0, len(rules)):
    if count_incidences(i, rule_to_index[rule]) >= num_valid_tickets:
      try:
        possibles[rule].append(i)
      except:
        possibles[rule] = [i]

absolute_rules = {}
done = False
while not done:
  for rule in possibles:
    if len(possibles[rule]) == 1:
      absolute_rules[rule] = possibles[rule][0]
  for rule in possibles:
    for rule2 in absolute_rules:
      if absolute_rules[rule2] in possibles[rule] and len(possibles[rule]) > 1:
        possibles[rule].remove(absolute_rules[rule2])
  if len(absolute_rules) >= len(possibles):
    done = True

print(absolute_rules)
total = 1
my_ticket = [83,53,73,139,127,131,97,113,61,101,107,67,79,137,89,109,103,59,149,71]
for rule in absolute_rules:
  if "departure" in rule:
    print(my_ticket[absolute_rules[rule]])
    print(total)
    total = total * my_ticket[absolute_rules[rule]]

print(total)
