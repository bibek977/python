content=True
i=1

with open("fileHandling/sample.txt","r") as f:
    while content:
        content=f.readline()

        if "bibek" in content.lower():   #For Lowercase sensetive
            print("Yes exist")
            print(content)
            print(i)
        i=i+1

