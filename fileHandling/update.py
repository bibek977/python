words=["bad","sad","worst"]
with open("fileHandling/another.txt","r") as f:
    text=f.read()
    

for word in words:
    text=text.replace(word,"@@#@$")

    with open("fileHandling/another.txt","w") as f:
        f.write(text)

word=input("Enter a word : ")

with open ("./f.txt",'r') as f:
    data=f.read()

data=data.replace("Python",word)

with open ("./f.txt",'w')as f:
    f.write(data)