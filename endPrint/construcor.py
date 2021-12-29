# class Intern:

#     def __init__(self):
#         print("Intern is avaialiable")

# bibek=Intern()

class Intern:

    def __init__(self,name,age,faculty):
        self.name=name    
        self.age=age  
        self.faculty=faculty    
        print("Hello")

    def getDetails(self):
        print("name: ",self.name)
        print("age: ",self.age)
        print("faculty: ",self.faculty)

    def getInfo(self):
        print(f"Hello, My name is {self.name} and I am {self.age} years old")

bibek=Intern("bibek",24,"programmer")
bibek.getDetails()

bibek.getInfo()