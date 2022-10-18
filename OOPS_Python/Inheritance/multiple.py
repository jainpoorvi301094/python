class Mother:
    mothername = ""
    def func1(self):
        print(self.mothername)

class Father:
    fathername = ""
    def func2(self):
        print(self.fathername)

class Son(Mother, Father):
    def func3(self):
        print("Mother:", self.mothername)
        print("Father:", self.fathername)

son=Son()
son.mothername="Siya"
son.fathername="Ram"

son.func2()
son.func1()
son.func3()