# def hello():
#     print("hello")

# hello()

def hello(name):
    # print("Hello ,", name)

    # greet=print("Good Morning,",name)
    # return greet

    wish="What's Up , " +name + "?"
    return wish

# hello("Bibek Bhattarai")


print(hello("Bibek Bhattarai"))

# bibek=hello("Bibek")
# print(bibek)


def sum(num1,num2):
    return num1+num2

print(sum(5,9))

n1=int(input("Enter a num: "))
n2=int(input("Enter a num: "))

s=sum(n1,n2)
print(s)