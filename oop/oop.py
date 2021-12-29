class Student:
    def showProfile(self):
        print(f"Name of the student is : {self.name}")
        print(f"Name of the student is : {self.rollNo}")
        print(f"Name of the student is : {self.subject}")

bibek=Student()
bibek.name="Bibek Bhattarai"
bibek.rollNo=161743
bibek.subject="Software"
bibek.showProfile()

class Employee:
    company="Google"
    salary="50k"

apeal=Employee()
bibek=Employee()
print(apeal.company)
print(bibek.company)
bibek.company="Facebook"
print(bibek.company)

# To change the company

Employee.company="Youtube"
print(apeal.company)

print(bibek.salary)
print(apeal.salary)
apeal.salary="70k"
print(apeal.salary)

Employee.salary="90k"
print(bibek.salary)