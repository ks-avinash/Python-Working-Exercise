class Student:
    grades=[]
    def __init__(self,name,id):
        self.name=name
        self.id=id
        
    def addGrade(self,grade):
        self.grades.append(grade)
    
    def showGrades(self):
        grds=''
        for grade in self.grades:
            grds+=str(grade)+' '
        return grds
    def show(self):
        return self.name +' ' +self.id + ' ' +stu1.showGrades()

stu1=Student('avinash','123')
stu1.addGrade(88)
stu1.addGrade(99)
stu1.addGrade(84)
print(stu1.showGrades())
print(stu1.show())
