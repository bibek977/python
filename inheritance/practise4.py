class Vector:

    def __init__(self,vec):
        self.vec=vec

    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k"

    def __add__(self,vec2):
        newList=[]
        for i in range(len(self.vec)):
            newList.append(self.vec[i]+vec2.vec[i])
        return Vector(newList)

v1=Vector([1,6,9])
v2=Vector([3,5,7])
print(v1)
print(v2)
print(v1+v2)