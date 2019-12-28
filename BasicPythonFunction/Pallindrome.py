n = 1331
temp = n
rev = 0
while n > 0:
    dig = n % 10
    rev = rev*10+dig
    n = n//10

if temp == rev:
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")


print("_________________________________________")

import copy

number = 136631
VAR = copy.deepcopy(number)
temp = 0

while number > 0:
    temp = temp * 10
    x = number % 10
    number = int(number / 10)
    temp = temp + x

if temp == VAR:
    print(" Pallindrome")
else:
    print("Not Pallindrome")