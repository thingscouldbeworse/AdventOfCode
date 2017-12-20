with open ("input.txt", "r") as myfile:
    inputStringList = myfile.readlines()
    checksum = 0
    for inputString in inputStringList[:-1]:
        inputString = inputString.replace("\n",'').split("\t")
        low = int(inputString[0])
        high = int(inputString[1])
        for num in inputString:
            num = int(num)
            if num < low:
                low = num
            if num > high:
                high = num
        checksum = checksum + (high - low)
    print(checksum)

