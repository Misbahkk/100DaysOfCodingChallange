"""Task 1: Creating a Class
Define a Python class called Person with attributes name and age. 
Write a method introduce() that prints out the name and age of the person."""


class Person:

    def __init__(self,name,age):
       self.name=name
       self.age=age
        

    def introduce(self):
        print(f'The Age of {self.name} is {self.age}.')
        

person1 =Person("misbah",26)
person2=Person("Radia",20)
person1.introduce()
person2.introduce()



"""TASK 1:
Create a class called Book with attributes like title, author, and number_of_pages. 
Write a method called describe that prints a description of the book including these attributes."""


class Book:
    def __init__(self,title,author,number_of_pages):
        self.title =title
        self.author = author
        self.number_of_pages = number_of_pages

    
    def description(self):
        print(f'The Book Title is {self.title} and Author is {self.author} and Number Of Page i read {self.number_of_pages}.')



book_info = Book("Jannat Ka Patty","Nimra Ahmed",193)
book_info.description()