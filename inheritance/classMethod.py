#To change the attributes of the class

class Bibek:
    permanent="Piluwa"

    def changaAddress(self,temp):
        self.__class__.permanent=temp

e=Bibek()
print(e.permanent)
e.changaAddress("Balkumari")
print(e.permanent)



class Bhattarai:

    rollNo=161743

    @classmethod
    def changeRollNo(cls,symNo):
        cls.rollNo=symNo

b=Bhattarai()
print(b.rollNo)
b.changeRollNo(17180067)
print(b.rollNo)