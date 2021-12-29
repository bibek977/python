name=input("Enter your name : ")
gender=input("Enter you gender : ")
name=name.capitalize()
gender=gender.capitalize()
if gender.startswith("M"):
    print("Hello MR. " + name)

elif gender.startswith("F"):
    print("Hello Mrs",name)

else:
    print("Hello " + name)

# name=input("Enter your name: ")
# gender=input("What's your gender: ")

# if(gender=="M" or gender== "m" or gender=="male" or gender=="Male" or gender=="MALE"):
#     print("Hello Mr." + name)

# elif(gender== gender=="F" or gender=="f" or gender=="female" or gender=="Female" or gender=="FEMALE"):
#     print("Hello Mrs." + name)

# else:
#     print("Inputs Error")


# name=input("Enter your name: ")
# gender=input("What's your gender: ")
# male=[ "M","m","male","Male","MALE"]
# female=["F","f","female","Female","FEMALE"]
# if(gender in male):
#     print("Hello Mr." + name)

# elif(gender in female):
#     print("Hello Mrs." + name)

# else:
#     print("Inputs Error")