# read() is mostly used to read binary files and it return string
# myFileVar.readline() read one line at a time
# myFileVar.readlines() read all lines in one go and retuen a list which contain all lines
################################################################################################33




# Define a path to your file in a variable called as myFilePath
myFilePath = "E:\\myNewPythonDir\\CompletePythonDeveloperCourse\\Module10\\sample.txt"

# Create Object myFile and open your file in Readonly Mode
myFile = open(myFilePath,'r')

# Iterate over file Line by Line
for myLine in myFile:
    if "Jabberwock".lower() in myLine.lower():
        print(myLine, end=" ")
# Close the file it is important
myFile.close()
print("_"*50)






# Use with method to open file , so you dont have to mention close file.
with open(myFilePath, "r") as myFile:
# Read file Line by Line
    for myLine in myFile:
        if "Jab".lower() in myLine.lower():
            print(myLine, end=" ")
print("_"*50)







# Use with method to open file , so you dont have to mention close file.
with open(myFilePath, "r") as myFile:
    myLine = myFile.readline()
# readline() function will read only one line , So if first line is read means file in not empty then enter into while loop in next statement and keep on iterate over file till the end of file reached
    while myLine:
        if "Jab".lower() in myLine.lower():
            print(myLine, end=" ")
        myLine = myFile.readline()
print("_"*50)










# Use with method to open file , so you dont have to mention close file.
with open(myFilePath, 'r') as myFile:
    myListOfLinesFromFile = myFile.readlines()  # readlines() will read entire contents of file in one go and returm list each line is converted into one element of list, This  may not be a very good idea when your file is large in size.
print(myListOfLinesFromFile) # unhash it to see the list of lines

for myLine in myListOfLinesFromFile:
    if "Jab".lower() in myLine.lower():
        print(myLine, end="")
print("#"*50)
# Read the list in reverse order
for myLine in myListOfLinesFromFile[::-1]:  # this will read lines in reverse order of file(which is stored in list)
    if "Jab".lower() in myLine.lower():
        print(myLine, end="")
print("_"*50)

















# Use with method to open file , so you dont have to mention close file.

with open(myFilePath, 'r') as myFile:
    myOneStringOfAllLines = myFile.read()  # read() will read entire contents of file in one go.
# read(size) >> size is an optional numeric argument and this func returns a quantity of data equal to size. If size if omitted, then it reads the entire file and returns it
# print(myOneStringOfAllLines) # unhash it to see that all lines are printed in one shot
for myChar in myOneStringOfAllLines[::-1]:     # It read complete file as one string and printed it in reverse order.
        print(myChar, end="")
























#####################################################################################################################################3
# FileMode    Description
# 'r'	Open a file for reading. (default)
# 'w'	Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
# 'x'	Open a file for exclusive creation. If the file already exists, the operation fails.
# 'a'	Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
# 't'	Open in text mode. (default)
# 'b'	Open in binary mode.
# '+'	Open a file for updating (reading and writing)
# default mode is rt (read text ) file


# Example
#               f = open("img.bmp",'r+b') # read and write in binary mode


# Note
# Unlike other languages, the character 'a' does not imply the number 97 until it is encoded using ASCII
# (or other equivalent encodings).
#
# Moreover, the default encoding is platform dependent. In windows, it is 'cp1252' but 'utf-8' in Linux.
#
# So, we must not also rely on the default encoding or else our code will behave differently in different platforms.
# Hence, when working with files in text mode, it is highly recommended to specify the encoding type.
# f = open("test.txt",mode = 'r',encoding = 'utf-8')



with open("test.txt",'w',encoding = 'utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")

#############################################################################################
# cat text.txt
# my first file
# This file
#
# contains three lines
#############################################################################################
f = open("test.txt",'r',encoding = 'utf-8')
print("This is file descriptior " + str(f.fileno()))
print(f.read(4))
print("Here are you " + str(f.tell()))
print("\n")
print(f.read(4))
print("Here are you " + str(f.tell()))
print("\n")
print(f.read())
print("Here are you " + str(f.tell()))
print("**********************************************")
print(f.read()) # when file reached end of file then read() return /n
print(f.read())
print(f.read())
print(f.read())
print("Here are you " + str(f.tell()))
print("Here are you " + str(f.tell()))
print("Here are you " + str(f.tell()))
print("**********************************************")
f.seek(0)
print("Here are you " + str(f.tell()))
f.close()