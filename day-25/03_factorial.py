"""Factorial Calculation:
Write a function to calculate the factorial of a given non-negative integer. 
The factorial of a number n is the product of all positive integers less than or equal to n."""


def factorial(n):
    tamp = 1
    if n <0:
        return "Only Calculate factorial Positive number "
    elif n == 0:
        return 1
    else:
        for i in range(1,n+1):
            tamp =i*tamp

        return tamp
    

try:
    fac = factorial(-3)
    print(fac)
except ValueError as e:
    print(e)

