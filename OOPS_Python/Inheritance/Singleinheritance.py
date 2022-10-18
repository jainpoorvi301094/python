class Parent:
    def func1(self):
        print("I am father func")

class Son(Parent):
    def func2(self):
        print("I am Son function")

son_object=Son()
son_object.func2()
son_object.func1()