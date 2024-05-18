"""Given an array of size n and a range [a, b]. The task is to partition the array 
around the range such that the array is divided into three parts.
1) All elements smaller than a come first.
2) All elements in range a to b come next.
3) All elements greater than b appear in the end.
The individual elements of three sets can appear in any order. You are required to 
return the modified array.....

Note: The generated output is 1 if you modify the given array successfully.

Geeky Challenge: Solve this problem in O(n) time complexity."""



class Solution:
    #Function to partition the array around the range such 
    #that array is divided into three parts.
	def threeWayPartition(self, array, a, b):
		
		n = len(array)
		low = 0
		high = n-1
		mid = 0
		while mid <= high:
			if array[mid] <= a:
				array[low],array[mid] =array[mid],array[low]
				
				low+=1
				mid+=1
			elif array[mid] > a and array[mid]<b:
				mid +=1
			else:
				array[high],array[mid] = array[mid], array[high]
				 
				high-=1
		print(array)
		return 1
		
# This is array
n = 15 
array = [10, 7, 6 ,1 ,4, 10 ,5, 2 ,7 ,5 ,3, 3, 8, 3, 8]
a, b = 5,5
arry_output = Solution()
modify_arry = arry_output.threeWayPartition(array,a,b)
print(modify_arry)
			
        
				
				
				
	    
	    
