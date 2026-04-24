class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        left, right = 0, len(nums)-1
        while right>=left:
            tmp = left + (right-left)//2
            if nums[tmp] > target:
                right = tmp-1
            elif nums[tmp] < target:
                left = tmp+1
            else:
                res = tmp
                break
        return res