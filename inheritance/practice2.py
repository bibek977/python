class Complex:

    def __init__(self,r,i):

        self.real=r
        self.imaginary=i

    def __add__(self,c):
        return Complex(self.real+c.real,self.imaginary+c.imaginary)

    def __mul__(self,m):
        return Complex(self.real*m.real-m.imaginary*self.imaginary,self.real*m.imaginary+m.real*self.imaginary)

    def __str__(self):
        return f"{self.real}+{self.imaginary}i"


c1=Complex(2,7)     
c2=Complex(5,1)      

print(c1+c2)
print(c1*c2)
print(c1)
print(c2)