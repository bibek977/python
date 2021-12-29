def studentId(name,id):
    return print(name,id)

student1=studentId("Bibek",161743)
student2=studentId("Apeal",161706)
# print(student1)


class Employeement:
    company="Google"

    def id(self):
        print(self.name)
        print(self.salary)
        print(self.company)


Employee1=Employeement()
Employee2=Employeement()
Employee1.name="Bibek"
Employee1.salary=400000
Employee2.name="Apeal"
Employee2.salary=500000

Employee1.id()
Employee2.id()

# class Student:
#     faculty="Engineering"

#     def std(self,name,rollNo):
#         print(name)
#         print(rollNo)
#         print(self.faculty)
#         print(self.batch)
# bibek=Student()
# bibek.faculty="Science and Tech."
# bibek.batch=2016
# bibek.std("Bibek",161743)

# apeal=Student()
# apeal.batch=2016
# apeal.std("Apeal",161703)