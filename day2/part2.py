with open ("input.txt", "r") as myfile:
    inputStringList = myfile.readlines()
    checksum = 0
    summation = 0
    for inputString in inputStringList[:-1]:
        inputString = inputString.replace("\n",'').split("\t")
        moment = 0
        for i in range(0,len(inputString)):
            for j in range(0,len(inputString)):
                if i != j:
                    if int(inputString[i]) % int(inputString[j]) == 0:
                        moment = int(int(inputString[i]) / int(inputString[j]))
                        print("dividing " + inputString[i] + " by " + inputString[j] + " = " + str(moment))
                        break
        print(summation)
        summation = moment + summation
    print(summation)
