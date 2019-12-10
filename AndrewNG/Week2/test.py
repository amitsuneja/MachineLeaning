def fun_first(a, b):
    return a+b

def fun_second(a, b):
    return fun_first(a, b)

x = fun_second(2,2)
print(x)