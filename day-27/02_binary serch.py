class Solution:	
	def binarysearch(self, arr, n, k):
		left = 0
		right = n-1
		while left <= right:
			mid = (left+right)//2
			if k == arr[mid]:
				return mid
			if k < arr[mid]:
				right= mid -1
			else:
				left = mid +1
		return -1
			
		

arr=[1,2,3,4,5]
n = len(arr)
k =4
binary_serch=Solution()	
x = binary_serch.binarysearch(arr,n,k)
print(x)	
        
		
