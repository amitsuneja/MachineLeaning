# id() is an inbuilt function in Python.
# id(object)

# As we can see the function accepts a single parameter and is used to return the identity(unique integer) of an object.
# This identity has to be unique and constant for this object during the lifetime.
# Two objects with non-overlapping lifetimes may have the same id() value

print('id of 5 =', id(5))

a = 5
print('id of a =', id(a))

b = a
print('id of b =', id(b))

c = 5.0
print('id of c =', id(c))
# Note id of 5,a,b will be same and c will be different in above code.

# This program shows various identities
str1 = "geek"
print(id(str1))

str2 = "geek"
print(id(str2))

# This will return True
print(id(str1) == id(str2))

# Use in Lists
list1 = ["aakash", "priya", "abdul"]
print(id(list1[0]))
print(id(list1[2]))

# This returns false
print(id(list1[0]) == id(list1[2]))