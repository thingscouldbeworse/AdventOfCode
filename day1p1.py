
with open('input1.txt', 'r') as inputfile:
    most = 0
    current = 0
    for row in inputfile:
        if row == "\n":
            if current > most:
                most = current
            current = 0
        else:
            current += int(row)

print(most)
