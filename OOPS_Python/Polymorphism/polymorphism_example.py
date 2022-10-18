class India:
    quality = 'best'  #class variable or static variable
    def capital(self):
        print("Delhi is capital of India")

    def language(self):
        print("Hindi is most widely spoken language")

    def type(self):
        print("India is developing country")

class USA:
    quality = 'best'
    def capital(self):
        print("Washington, D.C. is capital of India")

    def language(self):
        print("English is most widely spoken language")

    def type(self):
        print("USA is developed country")

obj_india=India()
obj_usa=USA()

for country in(obj_india, obj_usa):
    print(country.quality)
    country.capital()
    country.language()
    country.type()