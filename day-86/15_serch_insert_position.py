"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order."""



class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """


        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        
        return len(nums)
            
            


    

nums = [1,3,5,6]
target = 7

find_index = Solution()
index_num = find_index.searchInsert(nums,target)
print(index_num)