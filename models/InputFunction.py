# Take input from User as Strings

name=input("Enter your name : ")
print(type(name))
print(name)

number=input(" Enter a Number : ")
print(type(number))
number=int(number)
print(type(number))
print(number+5)

num=int(input("Enter a num : "))
print(num)
print(type(num))
print(num+number)


print(str(num)+str(number))
print(f"{str(num)}+{str(number)}")