class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = [1] * len(nums)
        res = 1
        for i, n in enumerate(nums):
            curMax = res
            for j in range(i):
                if nums[j]< n:
                    sub[i] = max(1+sub[j], sub[i])
                    res = max(curMax, sub[i])
        
        return res