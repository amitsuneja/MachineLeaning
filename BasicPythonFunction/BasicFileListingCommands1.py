import os


print("Current Working Directory = ", os.getcwd())
StartDir = os.getcwd()
print("changing directory to E:\\")
os.chdir("E:\\")
print("Changed Working Directory = ", os.getcwd())
print("HomeDirectory = ", os.path.expanduser('~'))
print("Changed Working Directory = ", os.path.join(StartDir, 'Dir1', 'Dir2'))
os.chdir(os.path.join(StartDir, 'Dir1', 'Dir2'))    # Note - never use '/Dir1' or '/Dir2'
print("Current Working Directory = ", os.getcwd())
entries = os.listdir()
for entry in entries:
    if os.path.isdir(entry):
        print("{} = directory name present in {}".format(entry, os.getcwd()))
    if os.path.isfile(entry):
        print("{} = file name present in {}".format(entry,os.getcwd()))
filefullpathname = os.getcwd() + "\\FileName01.txt"
print(" Full path for file ", filefullpathname)
(dirname, filename) = os.path.split(filefullpathname)
print("Extracted Directory Path =", dirname)
print("Extracted File name =", filename)
(shortname, extension) = os.path.splitext(filename)
print("File Extension=", extension)



