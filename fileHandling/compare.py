file3="fileHandling/sample2.txt"
file2="fileHandling/another.txt"
file1="fileHandling/sample.txt"

with open(file3,"r") as f:
    data=f.read()

with open(file2,"r") as f:
    content=f.read()

with open(file1,"r") as f:
    text=f.read()

if data==content:

    if data==text:
        print("All 3 are same")
    else:
        print("Both are same but no file 1")

elif content==text:
    print("both are same but no file 3")

elif data==text:
    print("Both are same but no file 2")

else:
    print("neither 3 of them are same")