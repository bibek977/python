with open('fileHandling/sample.txt','r') as f:
    text=f.read()

if "bibek" or "Bibek" in text:
    print("Exist")
else:
    print("Not Exist")

# print(text)