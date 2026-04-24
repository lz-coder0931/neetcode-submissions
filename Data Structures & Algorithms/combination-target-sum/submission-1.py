class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        sub = []
        def btrack(i):
            if sum(sub)==target:
                res.append(sub.copy())
                return
            if sum(sub)>target:
                return
            for j in range(i, len(nums)):
                sub.append(nums[j])
                btrack(j)
                sub.pop()

        btrack(0)

        return res




