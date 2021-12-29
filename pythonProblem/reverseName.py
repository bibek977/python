fname=input("Enter your first name : ")
lname=input("Enter your last name : ")

print("REverse order is : ",lname , ", ", fname)

n=len(fname)
print(n)
j=n
while j > 0:
    print(fname[j-1],end="")
    j=j-1

print("\t")

k=len(lname)
while k>0:
    print(lname[k-1],end="")
    k=k-1
print("\n")
fullname=fname+" "+lname

p=len(fullname)

while p>0:
    print(fullname[p-1],end="")
    p=p-1


print("\n")
# for i in fname:
#     print(i,end="")


name="Bibek Bhattarai"[::-1]
print(name)