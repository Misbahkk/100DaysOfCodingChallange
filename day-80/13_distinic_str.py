"""A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array."""
class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        count = {}
        distinic = []

        for string in arr:
            if string in count:
                count[string] = count[string]+1
            else:
                count[string]=1
                distinic.append(string)
        
        distinic =[s for s in distinic if count[s]==1]

        return distinic[k-1] if k <= len(distinic) else ""
        



obj = Solution()
arr = ["d","b","c","b","c","a"]
k = 2
disstr = obj.kthDistinct(arr,k)
print(disstr)