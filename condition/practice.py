text=input("Enter a text : ")

if "bachler student" in text:
    spam=True

elif text=="software engineering":
    spam=True

elif "python programming" in text:
    spam=True

else:
    spam=False

if(spam):
    print("This is spam message")
    print("you are " , text)

else:
    print("This is not spam message")