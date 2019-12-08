from functools import reduce
from functools import partial
import operator

"""
Understanding lambda
--------------------
SYNTAX:
-------
FunctionName = lambda argument_list: expression
sum_fun = lambda x, y: x + y
"""

list_a = list(range(5))  # [0, 1, 2, 3, 4]
list_b = list(range(10, 15))  # [10, 11, 12, 13, 14]
sum_fun = lambda x, y: x + y
print(sum_fun(list_a, list_b))  # [0, 1, 2, 3, 4, 10, 11, 12, 13, 14]
print(sum_fun(3, 4))  # 3+4=7
print("________________________________________________________________")


"""
Understanding Filter
--------------------
SYNTAX:
-------
filter(function, sequence)
The function filter(f,l) needs a function f as its first argument. 
f has to return a Boolean value, i.e. either True or False. 
This function will be applied to every element of the list l. 
Only if f returns True will the element be produced by the iterator, 
which is the return value of filter(function, sequence).
"""
fibonacci = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print(odd_numbers)   # 1, 1, 3, 5, 13, 21, 55]
even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)  # [0, 2, 8, 34]
print("________________________________________________________________")



"""
Understanding Reduce
--------------------
SYNTAX:
-------
reduce(function, sequence)
reduce continually applies the function func() to the sequence seq. It returns a single value.
if seq = [ s1, s2, s3, ... , sn ], calling reduce(func, seq) works like this:
At first the first two elements of seq will be applied to func, i.e. func(s1,s2) 
The list on which reduce() works looks now like this: [ func(s1, s2), s3, ... , sn ]
In the next step func will be applied on the previous result and the third element of the list, 
i.e. func(func(s1, s2),s3)
The list looks like this now: [ func(func(s1, s2),s3), ... , sn ]
Continue like this until just one element is left and return this element as the result of reduce()
"""

a = [1, 2, 10, 8]

my_function = lambda x, y: x+y
print(reduce(my_function, a))  # (1 + 2) = return 3
                               # (3 + 4) = return 6
                               # (6 + 4) = return 21
                               # Answer 21 is total sum of 1 + 2 + 10 + 8


my_function = lambda x, y: x if (x > y) else y
print(reduce(my_function, a))   # (1,2) =  return 2
                                # (2,10) = return 10
                                # (10,4) = return 10
                                #Answer  10 is biggest element value
print("________________________________________________________________")



"""
Understanding map 
--------------------
SYNTAX:
-------
r = map(func, seq)
The first argument func is the name of a function and the second a sequence (e.g. a list) seq. map() applies the 
function func to all the elements of the sequence seq. 
Before Python3, map() used to return a list, where each element of the result list was the result of the function func 
applied on the corresponding element of the list or tuple "seq". With Python 3, map() returns an iterator.
"""
def fahrenheit(T):
    return (float(9) / 5) * T + 32


def celsius(T):
    return (float(5) / 9) * (T - 32)


temperatures = (36.5, 37, 37.5, 38, 39)

temperatures_in_Fahrenheit = list(map(fahrenheit, temperatures))
temperatures_in_Celsius = list(map(celsius, temperatures_in_Fahrenheit))
print(temperatures_in_Fahrenheit)   # [97.7, 98.60000000000001, 99.5, 100.4, 102.2]
print(temperatures_in_Celsius)      # [36.5, 37.00000000000001, 37.5, 38.00000000000001, 39.0]
"""
In the example above we haven't used lambda. By using lambda, we wouldn't have had to define and name the functions 
fahrenheit() and celsius(). You can see this in the following interactive session
"""
C = [36.5, 37, 37.5, 38, 39]
F = list(map(lambda x: (float(9)/5)*x + 32, C))
C = list(map(lambda x: (float(5)/9)*(x - 32), F))
print(F)                              # [102.56, 97.7, 99.14, 100.4, 100.03999999999999]
print(C)                              # [39.2, 36.5, 37.300000000000004, 38.00000000000001, 37.8]
"""
map can be applied to more than one list. 
The lists don't have to have the same length. 
map() will apply its lambda function to the elements of the argument lists, 
i.e. it first applies to the elements with the 0th index, then to the elements with the 1st index until the n-th 
index is reached:
If one list has fewer elements than the others, map will stop when the shortest list has been consumed.
"""
a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5]

print(list(map(lambda x, y: x+y, a, b)))   # [18, 14, 14, 14]
print(list(map(lambda x, y, z: x+y+z, a, b, c)))   # [17, 10, 19]
print("________________________________________________________________")

"""
Understanding partial
--------------------
"""


def multiply(x, y):
    print("x=", x)
    print("y=", y)
    return x * y

# create a new function that multiplies by 2
multiply_it_by_2 = partial(multiply, 2)
# create a new function that multiplies by 3
multiply_it_by_3 = partial(multiply, 3)


print(multiply_it_by_2(4))
print(multiply_it_by_3(4))

# The 2 will replace x. y will equal 4 when double_it(4) is called.
"""
OUTPUT :
x= 2
y= 4
8
x= 3
y= 4
12
"""

print("Add of 1 + 1 =", operator.add(1, 1))

add100 = partial(operator.add, 100)
my_list = [1, 2, 3, 4, 5]
print(list(map(add100, my_list)))

"""
OUTPUT :
Add of 1 + 1 = 2
[101, 102, 103, 104, 105]
"""

string = "Hello, Python"
helloStr = partial(string.replace, "Python")

print(helloStr("Amit"))

"""
OUTPUT :
Hello, Amit
"""