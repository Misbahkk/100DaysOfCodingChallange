class Student:
    def __init__(self,name,score):
        self.name= name
        self.score = score

    def __repr__(self):
        return f'{self.name} : {self.score}'
        

students = [Student("Misbah",70),Student("Maadeha",80),Student("radia",67),Student("Laiba",56),Student("Mahma",95),Student("Aina",46)]
#Fine the average of scores 
#Firstly we do simple programing and then we do funtional programig


score_total = 0
for student in students:

    score_total += student.score

print(score_total/len(students))

#Know we do funtional programing uing reduce 

from functools import reduce

reduce_total = reduce(lambda total,student:student.score+total,students,0)
print(reduce_total/len(students))

#Challange 
#Multipy all thlist number each other 1*2*3=6

numbers = [1,2,3,4,5]

mul_num=reduce(lambda mul,number:number*mul,numbers,1)

print(mul_num)




