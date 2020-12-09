passports = []
passport = {}
num_valid = 0
with open('input.txt', 'r') as data:
  for line in data:
    if line == "\n":
      passports.append(passport)
      passport = {}
    else:
      fields = line[:-1].split(" ")
      for field in fields:
        left, right = field.split(":")
        passport.setdefault(left, right)

for passport in passports:
  if len(passport) == 8:
    num_valid += 1
  elif len(passport) == 7:
    valid = True
    for field in passport:
      if field == "cid":
        valid = False
    if valid:
      num_valid += 1
print(num_valid)
