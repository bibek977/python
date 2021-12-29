# Don't need to close the file

with open("fileHandling/sample.txt","r") as f:
    a=f.read()
print(a)

# with open("fileHandling/sample.txt","w") as f:
#     a=f.write("This is writting file handling .")
# print(a)