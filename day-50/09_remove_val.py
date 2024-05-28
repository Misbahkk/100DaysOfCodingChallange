# 27. Remove Element


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        
        :rtype: int
        
        """
        if not nums:
            return 0
        k=0
        n = len(nums)
        for i in range(0,n):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
            
        return k
nums = [0,1,2,2,3,0,4,2]
# nums = [3,2,2,3]
# nums =[2]
val = 2
remove= Solution()
k = remove.removeElement(nums,val)
print(nums[:k])
