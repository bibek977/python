class Train:

    def __init__(self,name,price,seats):
        self.name=name
        self.price=price
        self.seats=seats

    def getInfo(self):
        print(f"Traveller name is {self.name}")
        print(f"Price of 1 seat == {self.price}")

    def totalSeats(self):
        print(f"The number of seats is {self.seats}")

    def bookSeats(self):
        print(f"The booked seats are {self.seats}")
        self.seats=self.seats-1

    def cancelSeats(self):
        print(f"The cancelled seats are {self.seats}")
        self.seats=self.seats+1

name=input("Enter your name : ")
seats=int(input("How many seats you want to book : "))
Traveller1=Train(name,450,seats)

Traveller1.getInfo()
Traveller1.totalSeats()
for i in range(1,seats+1):
    Traveller1.bookSeats()

seats=int(input("Enter how many seats you want to cancel : "))
for i in range(1,seats+1):
    Traveller1.cancelSeats()