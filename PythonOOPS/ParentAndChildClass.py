class ClassA():
    var1 = 0
    var2 = 0
    def __init__(self):
        ClassA.var1 = 1
        ClassA.var2 = 2

    def methodA(self):
        ClassA.var1 = ClassA.var1 + ClassA.var2
        return ClassA.var1



class ClassB(ClassA):
    def __init__(self):
        print(ClassA.var1)
        print(ClassA.var2)

object1 = ClassA()
sum = object1.methodA()
print(sum)
print("_________________________________________")

object2 = ClassB()



print("_________________________________________")
print("_________________________________________")
print("_________________________________________")
print("_________________________________________")
print("_________________________________________")



class ClassA(object):
    def __init__(self):
        self.var1 = 1
        self.var2 = 2

    def methodA(self):
        self.var1 = self.var1 + self.var2
        return self.var1



class ClassB(ClassA):
    def __init__(self, class_a):
        self.var1 = class_a.var1
        self.var2 = class_a.var2

object1 = ClassA()
sum = object1.methodA()
object2 = ClassB(object1)
print(sum)
