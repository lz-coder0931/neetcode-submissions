class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False]*len(nums)
        dp[0] = True
        for i, step in enumerate(nums):
            end_index = min(i + step + 1, len(dp))
            for k in range(i, end_index):
                dp[k] = dp[i]

        return dp[-1]