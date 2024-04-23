import numpy as np
#User function Template for python3
class Solution:
    def firstElement (self, n):
        if n== 0:
            return 0
        elif n == 1:
            return 1
        
        fib_curn = 1
        fib_prev =0

        for _ in range(2,n+1):
            fib_next = (fib_curn+fib_prev)%1000000007
            fib_curn,fib_prev = fib_next,fib_curn

        return fib_curn

 
        

        # code here 



n= 4

matrix_num = Solution()
matrix_power = matrix_num.firstElement(n)
print(matrix_power)