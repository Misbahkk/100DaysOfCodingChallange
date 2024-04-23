# Write a program to find the sum of the given series 1+2+3+ . . . . . .(N terms) 
class Solution:
    def seriesSum(self, n : int) -> int:
        # code here
        sum=0
        for i in range(n+1):
            sum = i +sum
        return sum


n = 5
sum_obj = Solution()
sum_seri = sum_obj.seriesSum(n)
print(sum_seri)