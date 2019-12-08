# Decorator

def say_hello5():
    print("Hello5")


say_hello5()
print("__________________________________________________________________________________")


def say_hello6():
    return "Hello6"


my_hello6 = say_hello6()
print(my_hello6)
print("__________________________________________________________________________________")


# Functions can be passed as arguments to another function
def say_hello(my_var):
    print("Hello")
    my_var()


def say_hi():
    print("Hi")


say_hello(say_hi)
print("__________________________________________________________________________________")


# Functions can be defined inside another function
def say_hello9():
    print("Hello9")

    def say_hi9():
        print("Hi9")

    say_hi9()


say_hello9()
# say_hi9()  # Gives error as it is defined inside other function
print("__________________________________________________________________________________")
print("__________________________________________________________________________________")
print("__________________________________________________________________________________")


def say_hello11():
    print("Hello_11")

    def say_hi11():
        print("Hi_11")

    # return say_hi11()   --> this is incorrect way

    return say_hi11


my_var = say_hello11()
print(my_var)
my_var()
print("__________________________________________________________________________________")
print("__________________________________________________________________________________")
print("__________________________________________________________________________________")


# Another example with function arguments


def say_hello12(hello_var):
    print(hello_var)

    def say_hi12(hi_var):
        print(hello_var + " " + hi_var)

    return say_hi12


my_var = say_hello12("Hello")  # Print Hello and returns say_hi function which gets stored in say_hi_func variable

my_var("Hi")  # Call say_hi function and print "Hello Hi"
print("__________________________________________________________________________________")
print("__________________________________________________________________________________")
print("__________________________________________________________________________________")


# Decorators
# Callable objects are objects which accepts some arguments and returns some objects.
# functions and classes are examples of callable objects in Python.

# Decorators are callable objects which are used to modify functions or classes.

# Function decorators are functions which accepts function references as arguments
# and adds a wrapper around them and returns the function with the wrapper as a new function.


def decorator_func(some_func):
    # define another wrapper function which modifies some_func
    def wrapper_func():
        print("Wrapper function started")
        some_func()
        print("Wrapper function ended")

    return wrapper_func  # Wrapper function add something to the passed function and decorator returns the wrapper function


def say_hello15():
    print("Hello_15")


say_hello15 = decorator_func(say_hello15)
say_hello15()
print("__________________________________________________________________________________")
print("__________________________________________________________________________________")
print("__________________________________________________________________________________")
