# num1=int(input("Enter a num : "))
# num2=int(input("Enter a num : "))
# num3=int(input("Enter a num : "))
# num4=int(input("Enter a num : "))

# if num1<num2:
#     f1=num2
# else:
#     f1=num1

# if num3<num4:
#     f2=num4
# else:
#     f2=num3

# if f1<f2:
#     print(f"{f2} is greater")
# else:
#     print(f"{f1} is greater")

array=[]

n=int(input("how many number do you want to fill : "))

for i in range (1,n+1):
    num=int(input("Enter "+ str(i) + " number : "))

    array.append(num)

arr=max(array)

print(arr)


math=int(input("Enter the mask of math : "))
nepali=int(input("Enter the mask of nepali : "))
english=int(input("Enter the mask of english : "))
science=int(input("Enter the mask of science : "))

if(math>=45 and science>=45 and english>=45 and nepali>=45):
    print("Pass in all subject")
    if ((math+science+english+nepali)/4<=50):
        print("But Grade is Fail")
    else:
        print("And your grade is also Pass")
else:
    print("Your pass marks is less than pass value")