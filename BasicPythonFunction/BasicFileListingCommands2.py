"""

https://www.bogotobogo.com/python/python_files.php
"""


# The os.path.join() function can take any number of arguments
import os
import fnmatch

filefullpathname = "E:\\LenovoMyPythonProjects\\Practise\\BasicPythonFunction\\Dir1\\Dir2\\FileName01.txt"
DirfullPathname = "E:\\LenovoMyPythonProjects\\Practise\\BasicPythonFunction\\Dir1\\Dir2"
DirfullPathname_1 = "E:\\LenovoMyPythonProjects\\Practise\\BasicPythonFunction\\"

metadata = os.stat(filefullpathname)

print("mtime=", metadata.st_mtime)   # Actually, it's the number of seconds since the Epoch, which is defined
                                     # as the first second of January 1st, 1970.
print("st_atime=", metadata.st_atime)
print("st_ctime=", metadata.st_ctime)

import time

print(time.localtime(metadata.st_mtime))
# time.struct_time(tm_year=2018, tm_mon=11, tm_mday=7, tm_hour=17, tm_min=6, tm_sec=59,
# tm_wday=2, tm_yday=311, tm_isdst=0)

print(time.localtime(metadata.st_atime))
# time.struct_time(tm_year=2018, tm_mon=11, tm_mday=7, tm_hour=17, tm_min=6, tm_sec=59,
# tm_wday=2, tm_yday=311, tm_isdst=0)

print(time.localtime(metadata.st_ctime))
# time.struct_time(tm_year=2018, tm_mon=11, tm_mday=7, tm_hour=16, tm_min=49, tm_sec=58,
# tm_wday=2, tm_yday=311, tm_isdst=0)

print("metadata.st_size=", metadata.st_size)


listOfFiles = os.listdir(DirfullPathname)
pattern = "*.txt"
for entry in listOfFiles:
    if fnmatch.fnmatch(entry, pattern):
            print(entry)
########################################################################################################
# recursive listing
print("************************************************")

for root, dirs, files in os.walk(DirfullPathname_1):
    print("_____________")
    print("root =", root)
    for directory in dirs:
        print(directory)
    for filename in files:
        print(filename)

