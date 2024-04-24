"""You are standing on a point (x, y)
and you want to go to the origin (0, 0)
 by taking steps either left or down i.e. 
 from each point you are allowed to move either in 
 (x-1, y) or (x, y-1). Find the number of paths from point to origin.
"""


class Solution:
    def ways(self, n,m):
        #write you code here
        # Initialize a 2D array dp of size (x+1) x (y+1)
        dp = [[0]*(m+1) for _ in range(n+1)] 
        dp[0][0] = 1
        for i in range(n+1):
            for j in range(m+1):
                if i >0:
                    dp[i][j] += dp[i-1][j] 
                if j>0:
                    dp[i][j] += dp[i][j-1] 

                
        return dp[n][m] % 1000000007

x=3
y=0
path_obj = Solution()
calculate_num = path_obj.ways(x,y)
print(calculate_num)


# This approch to solve problem less time for big data
class Solution:
    def ways(self, n,m):
        #write you code here
        # Initialize a 2D array dp of size (x+1) x (y+1)
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

  # Base cases: Only one path from (0, 0) to itself and one path from any point on the edge 
  # (either x=0 or y=0) to the other edge point.
        for i in range(n + 1):
            dp[i][0] = 1  # All paths from points on the left edge (x=i, y=0) to the origin.
            for j in range(m + 1):
              dp[0][j] = 1  # All paths from points on the bottom edge (x=0, y=j) to the origin.

        # Fill the DP table iteratively.
        for i in range(1, n + 1):
                for j in range(1, m + 1):
                # Number of paths from current point is the sum of paths from the point below and the point to the left.
                  dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % 1000000007

        # Return the number of paths from (x, y) to (0, 0).
        return dp[n][m]
        

x=3
y=6
path_obj = Solution()
calculate_num = path_obj.ways(x,y)
print(calculate_num)
