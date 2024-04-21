"""Given an integer x, return true if x is a 
palindrome
, and false otherwise."""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_reverse = str(x)[::-1]
        if str(x) == x_reverse:
            return True
        else:
            return False


x=121 
reverse_integer =  Solution()
print(reverse_integer.isPalindrome(x))

