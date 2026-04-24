class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        sub = []
        added = set()
        def btrack(i):
            if i == len(nums):
                if tuple(sub) not in added:
                    added.add(tuple(sub))
                    res.append(sub.copy())
                return
            sub.append(nums[i])
            btrack(i+1)
            sub.pop()
            btrack(i+1)

        btrack(0)
        return res