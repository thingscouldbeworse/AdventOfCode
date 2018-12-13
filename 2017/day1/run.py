with open ("input.txt", "r") as myfile:
    inputString = myfile.readlines()[0].replace('\n', '')
    summation = []
    length = len(inputString)
    print(inputString)
    day2 = True
    if day2:
        elements_no = len(inputString)
        elements_no = int(elements_no/2)
    else:
        elements_no = 1

    inputString += inputString
    or i in range(0, length):
        #print("comparing " + inputString[i] + " and " + inputString[i+elements_no])
        if int(inputString[i]) == int(inputString[i + elements_no]):
            summation.append(int(inputString[i]))
    print(sum(summation)) 
