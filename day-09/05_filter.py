class Student:
    def __init__(self,name,score):
        self.name= name
        self.score = score

    def __repr__(self):
        return f'{self.name} : {self.score}'
        ###     

students = [Student("Misbah",70),Student("Maadeha",80),Student("radia",67),Student("Laiba",56),Student("Mahma",95),Student("Aina",46)]

student_result = []

for student in students:
    if student.name[0:1] == 'M':
      student_result.append(student)
    # if student.score < 70:
    #     student_result.append(student)


filter_list= list(filter(lambda student:student.name[0:1] == 'M', 
students))
# filter_list = list(filter(lambda student : student.score <70,students))
print(filter_list)
print(student_result)



numbers = [1,2,3,4,5,6,7,8,9,10]

filter_even =list(filter(lambda number: number%2==0,numbers))

print(filter_even)
