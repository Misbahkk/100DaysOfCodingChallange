"""Task for map():
Given a list of integers, create a new list where 
each element is the square of the corresponding element in the original list.

Example:
Input: [1, 2, 3, 4, 5]
Output: [1, 4, 9, 16, 25]"""


numbers =[1, 2, 3, 4, 5]
squre_num=list(map(lambda number: number**2,numbers))
print(squre_num)


"""2. filter():

Task: You have a list of student names and their ages, 
and you want to find the names of students who are 18 or older (eligible to vote)."""

class Can_Vote:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name}"
students = [Can_Vote("Alice", 20), Can_Vote("Bob", 16), Can_Vote("Charlie", 18)]



Voting_list=list(filter(lambda student: student.age >= 18,students))
print(Voting_list)



"""Task for reduce():
Given a list of numbers, find the maximum value in the list.

Example:
Input: [10, 7, 15, 3, 9]
Output: 15"""


numbers_reduse =[10, 7, 15, 3, 9]

from functools import reduce
num =reduce(lambda number:number == 15,numbers_reduse,1)
print(num)
