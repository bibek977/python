mydict={
    "bibek":{"full name" :"Bibek Bhattarai",
    "age" : 24,
    "address": "Balkumari",
    "college": "Ncit",
    "faculty": {"subject": "Software Engineering", "semester":7, "shift": "Day"},
    "language" : { "native": "nepali", "programming": "python"} },
    "apeal": {
        "full name": "Apeal tiwari",
        "age" : 24,
        "address": "kalanki",
        "college" : "Ncit"},
    "bipin": {
        "full name": "bipin ale",
        "age" : 23,
        "address": "satdobato",
        "college" : "Jawalakhel Csit College"},
    "anushil": {
        "full name": "anushil karki",
        "age" : 23,
        "address": "kaushal Taar",
        "college" : "Ncit"},
    }
# print("\n")
# name=input("Enter A Student name : ")
# print("\n")
# data=input("Enetr data : ")

# print("\n")
# print(mydict[name][data])
# print("\n")


# To change the data in the dict

# mydict['bipin']['age']=29

# print(mydict['bipin']['age'])

# To show the dictionary value keys
print(mydict.keys())

print(type(mydict.keys()))

# To change into the list

print(list(mydict.keys()))

# Print the keys and Values

print(mydict.values())

print(list(mydict.values()))

# print (key, value)

print(list(mydict.items()))

# print("\n")
# name=input("Enter A Student name : ")
# print("\n")
# data=input("Enetr data : ")

# print(mydict[name][data])

# print(list(mydict.keys()))
# print(list(mydict[name].values()))
# print(list(mydict[name][data].items()))
# print(list(mydict[name][data].keys()))

# To update the list in the dict add new value

newdict={
    "Owner": "Bibek"
}

mydict.update(newdict)
print(mydict)



# To update the value

updatedict={
    "Owner": "bibek"
}
mydict.update(updatedict)
print(mydict)

# print none as result as no error 

print(mydict.get("Owner"))



decesion=input("What dou you want to do : /n search /n change : ")
if decesion.lower()=="search":

    name=input("Enter a name : ")
    name.lower()

    data=input("Enter what you want to search : ")
    data.lower()

    print(mydict[name][data])
elif decesion.lower()=="change":
    name=input("Enter a name : ")
    name.lower()

    data=input("Enter what you want to search : ")
    data.lower()
    print(mydict[name][data])
    value=input("Enter What is the changed value : ")
    value.lower()
    student[name][data]=value
    print(mydict[name][data])

else:
    print("Type Error")