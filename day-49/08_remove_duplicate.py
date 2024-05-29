# 26. Remove Duplicates from Sorted Array


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        
        # k =1
        k=1





        
        n = len(nums)
        for i in range(1,n):
           if nums[i] != nums[k-1]:
               nums[k] = nums[i]
               k+=1
        return k
            

array = Solution()
nums=[1,2,2,3,4,4]
k= array.removeDuplicates(nums)
print(nums[:k])





