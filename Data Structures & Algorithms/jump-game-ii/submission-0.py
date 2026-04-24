class Solution:
    def jump(self, nums: List[int]) -> int:

        goal = len(nums)-1
        reach = len(nums) - 1
        res = 0
        while reach:
            for i in range(reach-1, -1, -1):
                if nums[i]+i >= goal:
                    reach = i
            goal = reach
            res+=1
        return res
            