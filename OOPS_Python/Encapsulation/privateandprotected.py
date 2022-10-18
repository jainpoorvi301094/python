#protected members defined by _a: can be access inside
#private member defined by __a

class Base:
    def __init__(self):
        self._a=2
        self.__c = "GeeksforGeeks"

class Derived(Base):
    def __init__(self):
        # Calling constructor of
        # Base class
        Base.__init__(self)
        print("calling protected members of class base:",self._a)
        # Modify the protected variable:
        self._a = 3
        print("Calling modified protected member outside class: ",
              self._a)
       # print("Calling private member of base class: ")
        #print(self.__c) will through attribute error

obj1=Base()
obj2=Derived()

# Calling protected member
# Can be accessed but should not be done due to convention

# Calling protected member
# Can be accessed but should not be done due to convention
print("Accessing protected member of obj1: ", obj1._a)

# Accessing the protected variable outside
print("Accessing protected member of obj2: ", obj2._a)