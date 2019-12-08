myCitiesList = ["CHD", "Gurgaon", "Ambala", "Delhi","Banglore", "Pune"]
myCitiesFile = "E:\\myNewPythonDir\\CompletePythonDeveloperCourse\\Module10\\myCities.txt"

with open(myCitiesFile,"w") as myCitesFileVar:
        for myCity in myCitiesList:
                # here = is not a assignment operator ,Hence no space required before and after equalto sign.
                # this is similar to end=" " in print statement
                # Flush is set to true then data is immediately written to drive (bypas the buffer)
                print(myCity, file=myCitesFileVar)
                # print(myCity, file=myCitesFileVar, flush="true")

myNewCitiesList = []
with open(myCitiesFile, "r") as myCitesFileVar:
        for myLine in myCitesFileVar:
                # strip() only remove character from begining or end
                myNewCitiesList.append(myLine.strip("\n"))

print(myNewCitiesList)


















AmitElda = "One", "Two", "Three"  # This is to guide you that it automatically treat it as a tuple
print(AmitElda)                   # ('One', 'Two', 'Three')

myAvar, myBvar, myCvar = AmitElda
print(myAvar)                    # One
print(myBvar)                    # Two
print(myCvar)                    # Three























imelda = "More Mayhem", "Imelda MAy", "2011", (
    (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz")
)

with open("E:\\myNewPythonDir\\CompletePythonDeveloperCourse\\Module10\\ImedlaFile.txt", "w") as imelda_File:
        print(imelda, file=imelda_File)
















with open("E:\\myNewPythonDir\\CompletePythonDeveloperCourse\\Module10\\ImedlaFile.txt", "r") as imelda_File:
        #  note complete statement is stored as a one line in file
        contents = imelda_File.readline()

print(contents)
print("*"*50)
myNewImelda = eval(contents)
# Notes
# 1. If we say myNewImelda = contents then it wont work
# 2. if we say myNewImelda = print(contents) then it wont work and give NULL to myNewImelda
# 3. If we say title, artist, year, track = contents , even then it wont work
print(myNewImelda)
print("*"*50)
title, artist, year, track = myNewImelda
print(title)
print(artist)
print(year)
print(track)
