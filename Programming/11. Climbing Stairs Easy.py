## dp[i] = dp[i-1] + dp[i-2]
## The step to step 1 is 1
## The step to step 2 is 2
## The step to step 3 is 1+2 = 3
## The step to step 4 is 3+2 = 5
## -> this is fibonacci series

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        if n == 3: return 3
        
        xi1 = 1
        xi2 = 2
        for i in range (3, n+1):
            xin = xi1+xi2
            xi1 = xi2
            xi2 = xin
        
        return xin
