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
  #print(passport)
  valid = True
  if len(passport) < 7:
    valid = False
  if len(passport) != 8 and 'cid' in passport:
    valid = False
  for field in passport:
    if field == 'byr':
      if int(passport['byr']) > 2002 or int(passport['byr']) < 1920:
        #print("invalid byr: " + str(passport['byr']))
        valid = False
    if field == 'iyr':
      if int(passport['iyr']) > 2020 or int(passport['iyr']) < 2010:
        #print("invalid iyr: " + str(passport['iyr']))
        valid = False
    if field == 'eyr':
      if int(passport['eyr']) > 2030 or int(passport['eyr']) < 2020:
        #print("invalid eyr: " + str(passport['eyr']))
        valid = False
    if field == 'hgt':
      if "cm" in passport[field]:
        if int(passport[field].split("cm")[0]) > 193 or int(passport[field].split("cm")[0]) < 150:
          #print("invalid hgt: " + str(passport[field]))
          valid = False
      elif "in" in passport[field]:
        if int(passport[field].split("in")[0]) > 76 or int(passport[field].split("in")[0]) < 59:
          #print("invalid hgt: " + str(passport[field]))
          valid = False
      elif "cm" not in passport[field] and "in" not in passport[field]:
        #print("invalid hgt: " + str(passport[field]))
        valid = False
    if field == 'hcl':
      if passport[field][0] != '#':
        #print("invalid hcl: " + str(passport[field]))
        valid = False
      elif not passport[field].split("#")[1].isalnum():
        #print("invalid hcl: " + str(passport[field]))
        valid = False
    if field == 'ecl':  
      if passport[field] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        #print("invalid ecl: " + str(passport[field]))
        valid = False
    if field == 'pid':
      if len(str(passport[field])) != 9:
        #print("invalid pid: " + str(passport[field]))
        valid = False
  if valid:
    print(passport)
    #print("valid")
    num_valid += 1
print(num_valid)
