data = []

with open('input.txt', 'r') as inputfile:
  for line in inputfile:
    dict_line = {}
    line = line.split(" ")
    dict_line["y_offset"] = int(line[2].split(",")[0])
    dict_line["x_offset"] = int(line[2].split(",")[1][:-1])
    dict_line["y_dim"] = int(line[3].split("x")[0])
    dict_line["x_dim"] = int(line[3].split("x")[1][:-1])
    dict_line["id"] = int(line[0].split("#")[1])
    data.append(dict_line)

fabric = []
for i in range(0,1001):
  fabric.append([0] * 1001)

singular_claims = []

for line in data:
  one_claim = True
  for i in range(0,line["y_dim"]):
    real_i = i + line["y_offset"]
    for j in range(0, line["x_dim"]):
      real_j = j + line["x_offset"]
      if fabric[real_i][real_j] == 0:
        fabric[real_i][real_j] = line["id"]
      else:
        one_claim = False
        if fabric[real_i][real_j] in singular_claims:
          singular_claims.remove(fabric[real_i][real_j])
  if one_claim:
    singular_claims.append(line["id"]) 

print(singular_claims)
