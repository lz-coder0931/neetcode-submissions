class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0]*(n+1)
        offset = 1

        for i in range(1,1+n):
            if i ==offset*2:
                offset = offset*2
            dp[i] = 1+dp[i-offset]
        
        return dp