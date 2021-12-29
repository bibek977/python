class Student:
    college="Ncit"

    def showDetails(self):
        print("This is a information about Student")


class Programmer(Student):
    language="Python"

    def getInfo(self):
        print(f"The student is a {self.language} Programmer")

    def showDetails(self):
        print(f"He is also a {self.college} student")

    def getId(self):
        print(f"The id is {self.id}")

std1=Student()
std2=Programmer()

std1.showDetails()
print(std1.college)

std2.showDetails()
std2.getInfo()
print(std2.college)
print(std2.language)

std2.id=161743
std2.getId()