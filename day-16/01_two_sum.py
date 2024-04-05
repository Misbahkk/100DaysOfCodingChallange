class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # sum the 2 numbers in the list and check that it is qual
        # to target number 
        for i in range(len(nums)):
            for j in range(len(nums)):
                sum = nums[i]+nums[j] 

                if sum == target and i !=j:
                    return [i,j]
                
            
nums = [3,2,4]
target = 6
number = Solution()
num_list= number.twoSum(nums,target)
print(num_list)
            


        