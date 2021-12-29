# Sets is a collection of non repetative elements 

a={1,3,5,6,9,2,3,2}
print(a)
print(type(a))

# Empty set
b=set()

# Adding elements
b.add(4)
b.add(5)
b.add(5)
b.add(7)

print(b)

# add tuple
b.add((1,4,6))
print(b)
l=len(b)
print(l)

print(b.pop())
print(b)

print(b.remove(4))
print(b)

print(b.pop())
print(b)

# print(b.remove(5))
# print(b)

b.clear()
print(b)


