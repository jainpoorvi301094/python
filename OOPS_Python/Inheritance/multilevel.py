class Grandfather:
    def __init__(self, grandfather):
        self.grandfather=grandfather

class Father:
    def __init__(self,father, grandfather):
        self.father=father

        # invoking constructor of Grandfather class
        Grandfather.__init__(self, grandfather)

class Son:
    def __init__(self, grandfather, father, son):
        self.son=son

        Father.__init__(self,father,grandfather)

    def print_name(self):
        print("grandfather_name:", self.grandfather)
        print("father_name:", self.father)
        print("son name:", self.son)

s1=Son("Dashrath","Ram", "Lav")
s1.print_name()

