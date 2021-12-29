class Vector2D:

    def __init__(self,i,j):
        self.icap=i
        self.jcap=j

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"

class Vector3D(Vector2D):

    def __init__(self,i,j,k):

        self.icap=i
        self.jcap=j
        self.kcap=k

    def __str__(self):
        return f"{self.icap}i+ {self.jcap}j + {self.kcap}k"


v2D=Vector2D(1,9)
v3D=Vector3D(4,7,2)

print(v2D)
print(v3D)