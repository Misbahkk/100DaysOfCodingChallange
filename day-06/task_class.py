"""Task 1: Creating a Class
Define a Python class called Person with attributes name and age. 
Write a method introduce() that prints out the name and age of the person."""


# class Person:

#     def __init__(self,name,age):
#        self.name=name
#        self.age=age
        

#     def introduce(self):
#         print(f'The Age of {self.name} is {self.age}.')
        

# person1 =Person("misbah",26)
# person2=Person("Radia",20)
# person1.introduce()
# person2.introduce()


"""Task 2"""
# class Person:

#     def __init__(self,name,age):
#        self.name=name
#        self.age=age
        

#     def introduce(self):
#         print(f'The Age of {self.name} is {self.age}.')

#     def change_name(self,new_name):
#        self.name = new_name
        
# print("This is Old name")
# person1 =Person("misbah",26)

# person1.introduce()
# print("This is a Change Name")
# person1.change_name("Radia")

# person1.introduce()






#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

"""Task : Inheritance
Create a subclass called Employee that inherits from the Person class. 
Add a new attribute position to the Employee class. 
Override the introduce() method to include the person's position."""

class Person:

    def __init__(self,name,age):
       self.name=name
       self.age=age
        

    def introduce(self):
        print(f'The Age of {self.name} is {self.age}.')

    def change_name(self,new_name):
       self.name = new_name
        

class Employee(Person):

    def __init__(self, name, age,position):
        super().__init__(name, age)
        self.position = position


    def introduce(self):
        print(f'The Age of {self.name} is {self.age} \n And her Positiion on Office is {self.position} ')


person1 =Employee("misbah",26,"Manager")

person1.introduce()
person1.change_name("Radia")
person1.introduce()






#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
"""TASK 3:
Create a class called Book with attributes like title, author, and number_of_pages. 
Write a method called describe that prints a description of the book including these attributes."""


# class Book:
#     def __init__(self,title,author,number_of_pages):
#         self.title =title
#         self.author = author
#         self.number_of_pages = number_of_pages

    
#     def description(self):
#         print(f'The Book Title is {self.title} and Author is {self.author} and Number Of Page i read {self.number_of_pages}.')



# book_info = Book("Jannat Ka Patty","Nimra Ahmed",193)
# book_info.description()


"""Task 4:
Create a class called Rectangle with attributes like width and height. 
Write methods to calculate the area and perimeter of the rectangle."""

# class Ractangle():

#     def __init__(self,width,height):
#         self.width = width
#         self.height = height

#     def area(self):

#         return self.width * self.height
       
#     def parameter(self):
#         return 2*(self.width+self.height)
    

# ractangle = Ractangle(20,40)
# Area = ractangle.area()
# Parameter = ractangle.parameter()

# print(f'The Are of Ractangel is {Area} and Parameter of Ractangele is {Parameter}')


#_____________________________________________________________
#_____________________________________________________________

"""Create a class called Animal with attributes like species and name. 
Create subclasses called Dog and Cat that inherit from Animal. 
Add a method called make_sound to the Animal class that prints a generic sound ("animal sound"). 
Override themake_sound method in the Dog and Cat subclasses to print specific sounds 
("woof" and "meow")."""





class Animal:

    def __init__(self,species,name):
        self.species = species
        self.name=name

    def make_sound(self):
        print("Animal sound")

class Dog(Animal):

    def __init__(self, name):
        super().__init__("dog", name)

    def make_sound(self):
        print("woof")


class Cat(Animal):

    def __init__(self, name):
        super().__init__("cat", name)

    def make_sound(self):
        
        print("meow")


animal = Animal("Unknown","Animal")
animal.make_sound()

Dog1 = Dog("Dog")
Dog1.make_sound()

cat1 = Cat("Cat")
cat1.make_sound()