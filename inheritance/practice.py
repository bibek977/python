class Pets:
    type="Mammel"

class Cat(Pets):
    pass

class Dog(Pets):

    @staticmethod
    def bark():
        print("vow vow")


d=Dog()
d.bark()

print(d.type)