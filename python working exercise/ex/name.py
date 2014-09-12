class Name:
    def __init__(self,first,middle,last):
        self.first=first
        self.middle=middle
        self.last=last
    def __str__(self):
        return self.first + ' ' +self.middle + ' ' +self.last
aName=Name=Name('avi','ks','kunue')
print(aName)