
"""Given two sorted arrays of size n and m respectively, find their union. 
The Union of two arrays can be defined as the common and distinct elements in the two arrays. """

class Solution:
        #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        i = 0
        j = 0

        union_arr=[]
        while i<n and j<m:
            if arr1[i] == arr2[j]:
                union_arr.append(arr1[i])
                i+=1
                j+=1
            elif arr1[i]<arr2[j]:

                union_arr.append(arr1[i])
                i+=1
            else:
                union_arr.append(arr2[j])
                j+=1

        while i <n:
            union_arr.append(arr1[i])
            i+=1
        while j<m:
            union_arr.append(arr2[j])
            j+=1


            
        

        union_arr = sorted(set(union_arr))
        return union_arr
    
arr1 = [-8, -3, -3, -2, 0, 1, 2, 2, 6]
arr2 = [-9, -9, 0]
n = len(arr1)
m=len(arr2)
union_arry = Solution()
x = union_arry.findUnion(arr1,arr2,n,m)
print(list(x))