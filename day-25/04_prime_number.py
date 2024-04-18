"""Prime Numbers:
Write a function to check if a given number is a prime number. 
The function should return True if the number is prime and False otherwise."""




def prime_number(num):

    if num == 1:
        return False
    elif num == 2:
        return True
    elif num > 1:
        for i in range(2,int(num**0.5)+1):
            if num%i == 0:
                return False
            
        return True
        

num = int(input("ENter number for find the prime number: "))
primenum = prime_number(num)
if primenum == False:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")
