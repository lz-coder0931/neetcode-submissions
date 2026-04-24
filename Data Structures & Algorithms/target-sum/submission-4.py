class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        if abs(target) > sum(nums) or (sum(nums) + target) % 2 != 0:
            return 0

        new_target = (target+sum(nums))//2

        dp = [0]*(new_target+1)
        dp[0] = 1

        for n in nums:
            for i in range(new_target, n - 1, -1):
                dp[i]+=dp[i-n]

        return dp[new_target]