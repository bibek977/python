with open("fileHandling/sample.txt","r") as f:
    data=f.read()
with open("fileHandling/sample2.txt","w") as f:
    f.write(data)