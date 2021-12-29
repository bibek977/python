f=open('fileHandling/sample.txt','r')

# data=f.read()
# data=f.read(5)
# print(data)

# text=f.readline()
text=f.readlines()
print(text)

new=open("fileHandling/another.txt", "r")
data=new.read()
print(data)

f.close()
new.close()