# The split() method breaks up a string at the specified separator
# and returns a list of strings.
# The split() method takes maximum of 2 parameters:
# separator (optional)- The is a delimiter.default Blank Space.
# maxsplit (optional) - The maxsplit defines the maximum number of splits.
# The default value of maxsplit is -1, meaning, no limit.

myText = 'I Love India'
# splits at space
print(myText.split())             # ['I', 'Love', 'u']


grocery = 'Milk, Chicken, Bread'
# splits at ','
print(grocery.split(', '))         # ['Milk', 'Chicken', 'Bread']


# Splitting at ':'
print(grocery.split(':'))           # ['Milk, Chicken, Bread']