class Begineer:
    platform="Portfolio"
    language="Any"

    def __init__(self):
        print("Initializing Begineer....")

    def getSalary(self):
        print("No salary for Begineer")

    def getHour(self):
        print("Any Time")


class Intermediate(Begineer):
    platform="Freelancing"
    language="Python"

    def __init__(self):
        super().__init__()
        print("Initializing Intermediate...")

    def getSalary(self):
        super().getSalary()
        print("The salary of intermediate is in $$")

    def getHour(self):
        super().getHour()
        print("Part Time")  

class Expert(Intermediate):
    platform="Company"
    language="All"

    def __init__(self):
        super().__init__()
        print("Initializing Expert....")

    def getSalary(self):
        super().getSalary()
        print("The Salary of Expert is $$$")

    def getHour(self):
        super().getHour()
        print("Full Time")

anees=Begineer()
print(anees.platform)
print(anees.language)
anees.getSalary()
anees.getHour()

anushil=Intermediate()
print(anushil.platform)
print(anushil.language)
anushil.getSalary()
anushil.getHour()

bibek=Expert()
print(bibek.platform)
print(bibek.language)
bibek.getSalary()
bibek.getHour()

# class Person:
#     country="Nepal"
#     salary=90000

#     def __init__(self):
#         print("Initializing Person......")
    
#     def takeBreathe(self):
#         print("I am Breathing...")

# class Employee(Person):
#     # country="Nepal"
#     # salary=90000

#     def __init__(self):
#         super().__init__()
#         print("Initialzing Employee....")

#     def getSalary(self):
#         print(f"The salary is {self.salary}")     #Get self.salary from above super class Person()

#     def takeBreathe(self):
#         super().takeBreathe()                    #take function from Person() and also gives to Programmer()
#         print("I am a Employee and I am also Breathing...")  #The second option is Person()

# class Programmer(Employee):
#     # country="Nepal"         
    
#     def __init__(self):
#         super().__init__()
#         print("Initializing Programmer.....")

#     def getSalary(self):
#         super().getSalary()                        #Get the function also running from above class Employee
#         print("No salary for Intern Programmer ")

#     def takeBreathe(self):
#         super().takeBreathe()                 #Get the function also run from class Employee
#         print("I am Programmer and Breathing...")  #The second option is Emplooyee() then 3rd is Person()


# p=Person()
# p.takeBreathe()
# print(p.country)

# e=Employee()
# e.takeBreathe()
# e.getSalary()

# pr=Programmer()
# pr.takeBreathe()
# pr.getSalary()
# print(pr.country)
