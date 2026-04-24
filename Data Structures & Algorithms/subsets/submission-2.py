class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        def backtracking(i):
            if i ==len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            backtracking(i+1)
            sub.pop()
            backtracking(i+1)
        backtracking(0)
        return res
            

            


