class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curMax = globMax = nums[0]

        for n in nums[1:]:
            curMax = max(curMax+n, n)
            globMax = max(globMax, curMax)
            print(globMax)

        return globMax
        