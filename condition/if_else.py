a=['bibek','apeal','anushil','bipin']

# if 'bibek' in a:
#     print("yes")

# else:
#     print("no")

name=input("Enter a name: ")

if name in a:
    print("Yes Exist")

elif name not in a:
    print("Error")

else:
    print("Does not Exist")


# num=int(input("Enter a num: "))

# if num>5:
#     print("greater than five")

# elif num>9:
#     print("greater than nine")

# elif num<90:
#     print("Less than ninty")

# else:
#     print("Error")


# num=int(input("Enter a num: "))

# if num>5:
#     print("greater than five")

# if num>9 and num==90:
#     print("greater than nine")

# if num is 90:
#     print("Its None")

# if not num>90:
#     print("Less than ninty")

# else:
#     print("Error")

num=int(input("Enter a number that you want to guess : "))

i=0
while i<1:
    n=int(input("Enter a number : "))

    if n==num:
        print("Correct Guess. WINNER ")
        break

    else:

        if n<num:
            print("Your guess is incorrect. Please Enter Higher number : ")
            
        elif n>num:
            print("Your guess is incorrect. Please Enter Lower number : ")

