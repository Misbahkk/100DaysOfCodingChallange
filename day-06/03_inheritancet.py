import random

#Mene Dog Class inherit ki ha Animal sa ab voo animal ki function or code ko access kr skta ha 

class Animal():
    info = "Animal Are Living THings they can sleep and eat"

    def __init__(self,name):
        print("This is Animal Class")
        self.name = name
        

class Dog(Animal):
    info = "The DOg IS very Cute"

    def __init__(self,name):
        #try to acess the __init__ f=method of Animal class
        #Python privide us to access the inheritance class method
        #through super
        super().__init__(name)
        print("This is Dog Class")
        self.number = random.randint(1,10)
        


class BullDog(Dog):
    
    def __init__(self, name):
        super().__init__(name)
        print("This is Bull Dog Class")





dog1 = BullDog("Hunny")
