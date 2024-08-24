# Row with a minimum number of 1's
#
# 
class Solution:
    def minRow(self,n,m,a):
        
        count = float('inf')
        row_index_min = 1
        min = 0
        for i in range(n):
            sum = 0
            for j in range(m):
                
                sum = a[i][j] +sum 
            min+=1
            if sum < count:
                    count = sum
                    row_index_min = min
        return row_index_min

        



# n = 3
# m = 3
# a = [[0, 0, 0],
#      [0, 0, 0], 
#      [0, 0, 0],
#     ]
n = 4
m = 4
a = [[1, 1, 1, 1],
     [1, 1, 0, 0], 
     [0, 0, 1, 1],
     [1, 1, 1, 1]]
matrix = Solution()
minimum_row = matrix.minRow(n,m,a)
print(minimum_row)
