"""Fibonacci Sequence:
Write a function to generate the Fibonacci sequence up to a specified number of terms. 
The function should take 
the number of terms as input and return a list containing the Fibonacci sequence."""

def fibbonic(n):
    a=0
    print(a)
    b=1
    print(b)
    c=a+b
    print(c)

    for i in range(1,n+1):

        a = b #1 1 2 3
        b = c #1 2 3 5
        c= a+b #2 3 5 13
        print(c)

fibbonic(8)


# Another to carete a list

def fibonic_list(n):
    fibo_list = []
    a,b = 0,1
    for _ in range(n+1):
        fibo_list.append(a)
        a,b = b,a+b
    return fibo_list

list_fib = fibonic_list(8)
print(list_fib)