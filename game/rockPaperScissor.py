import random

def game(comp,you):

    if comp==you:
        return None

    elif comp=="r":
        if you=="p":
            return True
        else:
            return True

    elif comp=="s":
        if you=="p":
            return False
        else:
            return True
    else:
        if you=="s":
            return True
        else:
            return False

n=random.randint(1,3)

if n==1:
    comp="r"

elif n==2:
    comp="p"

else:
    comp="s"

print("Computer has Chosen : ")

m=input("Enter your choice : \n Rock \n Paper \n Scissor : ")

if m.lower()=="rock":
    you="r"

elif m.lower()=="paper":
    you="p"

elif m.lower()=="scissor":
    you="s"

else:
    print("Type Error")

g=game(comp,you)

print("Computer choose : ",comp)
print("You choose : ",you)

if g==None:
    print("Tie")
elif g:
    print("You Won ")

else:
    print("You Loose")






# import random

# def game(comp,you):
    
#     if comp==you:
#         return None
    
#     elif comp=="r":
#         if you=="p":
#             return True
#         elif you=="s":
#             return False

#     elif comp=="p":
#         if you=="s":
#             return True
#         elif you=="r":
#             return False

#     elif comp=="s":
#         if you == "r":
#             return  True
#         elif you == "p":
#             return False

# print("Computer turn 1. Rock == r  2. Paper == p  3. Scissor == s ?  ")

# n=random.randint(1,3)

# if n==1:
#     comp="r"

# elif n==2:
#     comp="p"

# elif n==3:
#     comp="s"

# you=input("Your's turn 1. Rock == r  2. Paper == p  3. Scissor == s ?   ")

# w=game(comp,you)

# print("Comp choose ",comp)
# print(" You choose ",you)

# if w==None:
#     print("Tie")
# elif w:
#     print("Win")
# else:
#     print("Loose")

