def fact(n):
    factorial=1
    for i in range(n):
        factorial=factorial*(i+1)

    return factorial

# print(fact(6))

f1=fact(5)
print(f1)

# For recursive function

# z=int(input("Enter a num: "))

def recursive(n):
    if n==1 or n==0:
        return 1
    return n*recursive(n-1)

print(recursive(5))

# Find the maximum

num1=int(input("Enter a num1: "))
num2=int(input("Enter a num2: "))
num3=int(input("Enter a num3: "))

def maximum(num1,num2,num3):
    if (num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

m=maximum(num1,num2,num3)
print(f"The maximum num is : {m}")
print(m)