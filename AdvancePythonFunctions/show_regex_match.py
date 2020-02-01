#!/bin/python3
import re
sourcefile="AMAZRUSEASQ3D01.rpm.sorted"
targetfile="AMAZRUSEASQ3D01.rpm"
source_linelist = list()
def show_regex_match(text, regex):
    """
    Prints the string with the regex match highlighted.
    """
    print(re.sub(f'({regex})', r'\033[1;30;43m\1\033[m', text))


with open(sourcefile, "r") as source, open(targetfile, "w") as target:
        s_linelist = source.readlines() # this will add \n in end of elements of lines
        for line in s_linelist:
                line = line.rstrip('\n')
                line = line.rstrip(".noarch")
                line = line.rstrip(".x86_64")
                pattern = r"-\d*(.|-)\d*(.|-)\d*(.|-)\d*(.|-)\d*(.|-)\d*(.|-)\d*"
                #pattern = r"-\d.\d*"
                show_regex_match(line,pattern)
                source_linelist.append(line)
#print(source_linelist)
