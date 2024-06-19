class Student:
    def __init__(self,name,marks):
        self.naem = name
        self.marks = marks
    
    def avg(self):
        sum = 0
        for i in self.marks:
            sum +=i

        print(f"Hi!! {self.naem} Avrage of All subject: ",sum/len(self.marks))
       



s1 = Student("Misbah" ,[99,97,98])
print(s1.naem, s1.marks)
s1.avg()

        

        