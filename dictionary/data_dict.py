# full_name= {}
# student1=input("Enter your Name: ")
# student11=input("Enter your Name: ")
# student2=input("Enter your surname: ")
# student22=input("Enter your surname: ")

# full_name[student1]=student11
# full_name[student2]=student22


# print(full_name)


names={}

n=int(input("Enter how many names you want to save : "))

for i in range(n):

    name=input(str(i+1)+"==> Enter first name : ")
    sur_name=input(str(i+1)+"==> Enter Last name : ")

    names[name]=sur_name

print(names)

fullName={}

# n=int(input("Number of student : "))

# for i in range (n):

#     fname=input("Enter Your name : ")
#     lname=input("Enter your surname : ")

#     fullName[fname]=lname

# print(fullName)


school={}

n=int(input("How many batch do you want to save : "))

for i in range(n):

    batch=input("Which Batch : ")
    m=int(input("How many students : "))

    for j in range(m):
        name=input("Enter name : ")
        surname=input("Enter surname : ")
        school[batch]={name,surname}
               
print(school)