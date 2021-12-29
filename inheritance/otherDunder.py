class Number:

    def __init__(self,num):
        self.num=num

    def __str__(self):
        return f"Decimal num : {self.num}"

    def __len__(self):
        return 1

n=Number(90)
print(n)
print(len(n))