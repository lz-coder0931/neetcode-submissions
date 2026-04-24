class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        def backtracking(i):
            res.append(sub.copy())
            for j in range(i,len(nums)):
                sub.append(nums[j])
                backtracking(j+1)
                sub.pop()
        backtracking(0)
        return res
            

            


