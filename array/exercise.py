# Exercise NO .1

# F1=input("Fruit 1=")
# F2=input("Fruit 2=")
# F3=input("Fruit 3=")
# F4=input("Fruit 4=")
# F5=input("Fruit 5=")
# F6=input("Fruit 6=")
# list=[F1,F2,F3,F4,F5,F6]
# print(list)

fruits=[]
num=int(input("How many fruits do you have : "))
for i in range(num):
    name=input(f"Enter the name of the fruit no {i+1} : ")
    fruits.append(name)
    i+=1

print(fruits)




# sum of list

list1=[4,6,7,9]
list2=[1,4,2,7]
list3=list1+list2
# list1.append(list2)

print(list3)
list3.sort()
print(list3)


arr1=[2,7,9,3,4]
print(arr1[0]+arr1[1]+arr1[2]+arr1[3]+arr1[4])
print(sum(arr1))

