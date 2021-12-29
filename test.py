fruits=[]

n=int(input("How many fruits do you want to add : "))

for i in range (n):
    fruit=input(f"Enter name of a fruit {i} : ")
    fruits.append(fruit)
    i+=1

print(fruits)