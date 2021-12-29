# sets={1,6,9,4,8}
# print(sets.union({4,11,1}))
# print(sets.intersection({4,11,1}))

num1=int(input("Enter how many values you want to save in set1 : "))
set1=set()
for i in range(num1):
    n=int(input("Enter number sets: "))
    set1.add(n)

print(set1)

num2=int(input("Enter how many values you want to save in set2 : "))
set2=set()
for i in range(num2):
    n=int(input("Data are : "))
    set2.add(n)

print(set2)


num3=int(input("Enter how many values you want to save in set3 : "))
set3=set()
for i in range(num3):
    n=int(input("Data are : "))
    set3.add(n)

print(set3)


intersection=set1.intersection(set2)
print(intersection)

union=set1.union(set3)
print(union)
