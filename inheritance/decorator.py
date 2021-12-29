# class Employee:

#     company="Google"
#     salary=50000
#     bonusSalary=10000

#     def totalSalary(self):
#         return self.salary + self.bonusSalary

# e=Employee()
# print(e.totalSalary())

# To show with out e.totalSalary() @property shows as e.totalSalary

class Employee:

    company="Google"
    salary=50000
    bonusSalary=10000

    @property                                   #Getter method
    def totalSalary(self):
        return self.salary + self.bonusSalary

    def plusSalary(self):
        return self.totalSalary + 15000

    @totalSalary.setter              #Setter method
    def totalSalary(self,value):
        self.salary=value-self.bonusSalary

e=Employee()
print(e.salary)
print(e.bonusSalary)
print(e.totalSalary)     #We dont use () in the e.totalSalary
print(e.plusSalary())

e.totalSalary=51000
print(e.bonusSalary)
print(e.salary)
print(e.plusSalary())