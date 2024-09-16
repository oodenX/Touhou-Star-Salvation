
class A:
    def __init__(self):
        self.a = 1

class B:
    def __init__(self):
        self.b = A

class C(B):
    def __init__(self):
        self.c = 3

class parent:
    def __init__(self, name):
        self.name = name
    def print_name(self):
        print(self.name)

class child(parent):
    def __init__(self, name, age):
        self.age = age
        super().__init__(name)
    def print_name(self):
        # super().print_name()
        print("这个人的年龄是：", self.age)

people = child('Tom', 10)
people.print_name()