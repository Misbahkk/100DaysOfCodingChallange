"""2. Write a Python program that calculates the factorial of a given positive integer, 
but with the restriction that you cannot use any 
built-in factorial functions or libraries or loops (e.g., math.factorial)."""


def fact(num):
    if num == 0 or num == 1:
        return 1
    
    return num*fact(num-1)


num = int(input("Enter a number to calculate factorial: "))
factorial = fact(num)
print(f"Factorial of {num}! is: {factorial}")
