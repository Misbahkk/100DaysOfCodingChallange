class Solution(object):
    def rangeSum(self, nums, n, left, right):
        """
        :type nums: List[int]
        :type n: int
        :type left: int
        :type right: int
        :rtype: int
        """
        Mod = 10**9 +7 #Define the mode
        subarrays = []
        for start in range(len(nums)):
            for end in range(start,len(nums)):
                subarray =  nums[start:end+1]
                sums = 0
                for sub in range(len(subarray)):
                    sums = subarray[sub]+sums
                

                subarrays.append(sums)
        subarrays.sort()
        count = 0
        for num in range(left-1,right):
            count = (subarrays[num]+count)%Mod
            print(count)


        return count

            



obj = Solution()
nums = [1,2,3,4]
n = 4
left = 1
right = 5
sum_nums = obj.rangeSum(nums,n,left,right)
print(sum_nums)