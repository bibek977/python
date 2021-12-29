class Calculator:

    def __init__(self,num):
        self.num=num

    def square(self):
        print(f"The square of {self.num} is {self.num**2}")
    def squareRoot(self):
        print(f"The square root of {self.num} is {self.num**0.5}")
    def cube(self):
        print(f"The cube of {self.num} is {self.num**3}")


a=Calculator(4)

a.square()
a.squareRoot()
a.cube()


class Bibek:
    surname="bhattarai"

    def __init__(self,name):
        self.name=name
        print(self.name)
        print(self.surname)


b=Bibek(name="Bibek")


class Bibek:
    surname="bhattarai"
    name="BIBEK"
    rollno=17180067
    address="Piluwa Bara"

    def __init__(self):
        pass

    def getName(self):
        print("My name is : ",self.name)
        print("My surname is : ",self.surname)
    def getRollNo(self):
        print("roll no :"+ str(self.rollno))

    def getAddress(self):
        print(f"add = {self.address}")




c=Bibek()
c.getAddress()
c.getName()
c.getRollNo()

d=Bibek()
d.name="anees"
d.getAddress()
d.getName()
d.getRollNo()


class Bibek:
    surname="bhattarai"

    def __init__(self,name,rollno,address):
        self.name=name
        self.rollno=rollno
        self.address=address

    def getName(self):
        print("My name is : ",self.name)
        print("My surname is : ",self.surname)
    def getRollNo(self):
        print("roll no :"+ str(self.rollno))

    def getAddress(self):
        print(f"add = {self.address}")


b=Bibek(name="Bibek",rollno=161743,address="balkumari")
b.getAddress()
b.getName()
b.getRollNo()


c=Bibek("Bhattarai",17180067,"Piluwa, Bara")
c.getAddress()
c.getName()
c.getRollNo()
