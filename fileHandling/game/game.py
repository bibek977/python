import random

print("Welcome to the game......")

computer=random.randint(1,100)

# print(computer)

user=None
guess=0

while (user!=computer):
    user = int(input("Guess the number: "))
    guess+=1

    if user==computer:
        print("You guessed it right.")

    else:
        print("You gussed it wrong..")

        if user<computer:
            print("Guess Higher...")
        else:
            print("Guess Lower")
print(f"Your guess score is {guess} ")


with open ("filehandling/game/highscore.txt","r") as f:
    score=f.read()

if int(score)>guess:
    print("You've broken high score")
    with open ("filehandling/game/highscore.txt","w") as f:
        f.write(str(guess))