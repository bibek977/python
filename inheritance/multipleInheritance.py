class Programmer:
    college="Ncit"
    rollNo=161743

class Student:
    college: "HSM"
    level=11

    def upgradeLevel(self):
        self.level=self.level + 1

class Bibek(Programmer,Student):
    name="Bibek"
    language="Python"

b=Bibek()

print(b.college)   # Prints Ncit bacause class Programmer assigned first in class Bibek
print(b.rollNo)
print(b.college)
print(b.level)

b.upgradeLevel()   # Upgrading the lavel
print(b.level)
print(b.language)
print(b.name)
