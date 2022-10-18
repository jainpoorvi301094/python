from datetime import date
class Person:
    def __init__(self,age,name):
        self.age=age
        self.name=name
    # a class method to create a Person object by birth year.
    @classmethod
    def frombirthyear(cls, name, year):
        return cls(name, date.today().year-year)

    @staticmethod
    def isAdult(age):
        return age>18


person1=Person(25, "avi")
person2=Person.frombirthyear("arav", 2000)
print(person2.age)
print(Person.isAdult(22))

