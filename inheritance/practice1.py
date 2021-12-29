class Employee:

    salary=50000
    salaryIncrement=1.5

    @property
    def totalSalary(self):
        return self.salary*self.salaryIncrement

    @totalSalary.setter
    def totalSalary(self,value):
        self.salaryIncrement=value/self.salary

e=Employee()
print(e.totalSalary)
e.totalSalary=70000
print(e.salaryIncrement)