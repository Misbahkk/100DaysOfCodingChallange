# Value equal to index value
"""Given an array Arr of N positive integers. Your task is to find 
the elements whose value is equal to that of its index value ( Consider 1-based indexing )"""


class Solution:

	def valueEqualToIndex(self,arr, n):
		ans = []
		for i in range(n):
			# print(arr[i])
			if arr[i] == i+1:
				ans.append(i+1)
		if not ans:
			return [-1]
		return ans
		# code here


arr=[15,2,3,32,6]
n=5
value_index = Solution()
value = value_index.valueEqualToIndex(arr,n)
print(value)