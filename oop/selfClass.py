# class Employee:
#     company="Facebook"

#     def getSalary(self):
#         # print("Salary = 50k")
#         print("Salary =",self.salary)

# bibek=Employee()

# bibek.salary=50000
# bibek.getSalary()   # It is == Employee.salary(bibek) so self is used

class Employee:
    company="Facebook"

    def getSalary(self,greet):
        # print("Salary = 50k")
        print("Salary =",self.salary)
        print(" ",greet)

bibek=Employee()

bibek.salary=50000
bibek.getSalary("Thanks")   # It is == Employee.salary(bibek) so self is used

