
#When ever you creat something from a classit's called aeither an instance or object
"""Instance Reference: self is used to access variables and methods associated with the current 
instance of the class within the method.

Instance-specific Operations: When a method is called on an instance of a class, self allows 
the method to operate on the data unique to that instance (i.e., instance variables).

Method Invocation: It helps Python distinguish between instance variables 
(attributes) and local variables within the method. Without self, Python would assume that a 
variable is local to the method rather than an attribute of the instance."""

import random

class Dog:
    info = "The DOg IS very Cute"

    def __init__(self,name):
        print("I am The Lucky")
        self.number = random.randint(1,10)
        self.name = name




dog1 = Dog("Hunny")
dog2 = Dog("Cati")

print(dog1.number,dog1.name)
dog1.name = 'bunny'
print(dog2.number)
print(dog1.name)