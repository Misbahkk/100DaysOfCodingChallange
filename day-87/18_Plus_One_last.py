class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digit = ''.join(map(str,digits))
        digit = int(digit)+1
        digit = [int(digit) for digit in str(digit)]
        return digit        




digits = [4,6,8,9]
last_vari = Solution()
puls_one = last_vari.plusOne(digits)
print(puls_one)