class Student:
    def __init__(self,name,score):
        self.name= name
        self.score = score

students = [Student("Misbah",70),Student("Maadeha",80),Student("radia",67),Student("Laiba",56),Student("Mahma",95),Student("Aina",46)]


student_result=[]

for student in students:


    # if student.score >=70:

    #     student_result.append(f"{student.name} Passed")

    # else:
      
    #     student_result.append(f"{student.name} Fail")

    #This line Output is same above code

    student_result.append(f"{student.name} Passed") if student.score >=70 else student_result.append(f"{student.name} Fail")
    
map_result = list(map(lambda student:f"{student.name} Passed" if student.score >=70 else f"{student.name} Fail" ,students))


print(map_result)

print(student_result)

#Challange 
#Provide a list you task is multipy this list number by 2

numbers = [2,4,6,8,10]

number_mul=list(map(lambda number:number*2,numbers))
print(number_mul)