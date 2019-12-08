"""
Target : This program will prompt for a number.
Then it will pass that number to function .
Function will calculate its factorial and return the answer.
Then answer will be printed.

https://stackoverflow.com/questions/11356168/return-in-recursive-function


"""


def calculate_factorial(my_num):
    """Function to return the factorial
    of a number using recursion"""
    if my_num == 1:
        return my_num
    else:
        return my_num * calculate_factorial(my_num - 1)


num = int(input("Please enter the number:"))

if num <= 1:
    print("you are an idiot")
else:
    result = calculate_factorial(num)
    print("{}! = {}".format(num, result))