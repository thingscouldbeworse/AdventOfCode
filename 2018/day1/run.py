import sys
with open('input.txt', 'r') as inputfile:
    data = []
    for line in inputfile:
        data.append([line[0], int(line[1:])])
    total = 0
    totals = []
    totals.append(0)
    while True:
        for item in data:
            if item[0] == '-':
                total -= item[1]
            else:
                total += item[1]           
        
            if total in totals:
                print(total)
                sys.exit(1)
            totals.append(total)       
        