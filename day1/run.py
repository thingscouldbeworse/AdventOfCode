with open ("input.txt", "r") as myfile:
    inputString = myfile.readlines()[0].replace('\n', '')
    summation = []
    inputString += inputString[0]
    for i in range(0, len(inputString)-1):
        if int(inputString[i]) == int(inputString[i+1]):
            summation.append(int(inputString[i]))
    print(sum(summation)) 
