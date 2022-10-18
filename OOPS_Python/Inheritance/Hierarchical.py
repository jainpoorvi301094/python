class Parent:
    def parent(self):
        print("I am Parent")

class Child1(Parent):
    def child1(self):
        print("I am first child")

class Child2(Parent):
    def child2(self):
        print("I am second child")

obj1=Child1()
obj2=Child2()
obj1.child1()
obj1.parent()
obj2.child2()
obj2.parent()