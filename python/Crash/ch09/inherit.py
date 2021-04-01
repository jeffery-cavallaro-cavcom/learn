class SuperOne:
    super_one_value = 1

    def __init__(self, value):
        self.ivalue = value

    def show(self):
        print(self.ivalue)


class SuperTwo:
    super_two_value = 2

    def __init__(self, value):
        self.svalue = value


class SimpleChild(SuperOne):
    def __init__(self, ivalue, fvalue):
        super().__init__(ivalue)
        self.fvalue = fvalue

    def show(self):
        print(self.fvalue)


class Child(SuperOne, SuperTwo):
    def __init__(self, ivalue, svalue, fvalue):
        SuperOne.__init__(self, ivalue)
        SuperTwo.__init__(self, svalue)
        SuperTwo(svalue)
        self.fvalue = fvalue


obj1 = SimpleChild(100, 1.414)
print(obj1.super_one_value)
print(obj1.ivalue)
print(obj1.fvalue)
obj1.show()  # Override

obj2 = Child(42, "Hello", 3.14)
print(obj2.super_one_value)
print(obj2.super_two_value)
print(obj2.ivalue)
print(obj2.svalue)
print(obj2.fvalue)
obj2.show()  # No override
