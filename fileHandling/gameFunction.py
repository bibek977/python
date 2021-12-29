def game():
    return 7

score=game()

# with open("fileHandling/highScore.txt","r") as f:
#     highscore=int(f.read())

# if score>highscore :
#     with open("fileHandling/highScore.txt","w") as f:
#         f.write(str(score))

# print(highscore)


# For blank highscore text file

with open("fileHandling/highScore.txt") as f:
    highScore=f.read()

if highScore=="":
    with open("fileHandling/highScore.txt","w") as f:
        f.write(str(score))

elif (score>int(highScore) or highScore==""):
    with open("fileHandling/highScore.txt","w") as f:
        f.write(str(score))

print(highScore)