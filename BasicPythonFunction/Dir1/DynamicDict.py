myDict = {}

for i in range(1, 10, 2):
    myDict["myString"+str(i)] = "Hello"

for myKey,myValue in myDict.items():
    print("Key is {0} =  {1}".format(myKey,myValue))

# Key is myString1 =  Hello
# Key is myString3 =  Hello
# Key is myString5 =  Hello
# Key is myString7 =  Hello
# Key is myString9 =  Hello