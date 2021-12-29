text="      Hello bibek   "
print(text)

print(text.strip())



def replace_and_strip(string,word):
    newString=string.replace(word,"")
    return newString.strip()

string="      hello mr bibek bhatarai  "
r=replace_and_strip(string,"bibek")
print(r)