class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for n in nums:
            ls = nums.copy()
            ls.remove(n)
            remain = target - n
            if remain in ls:
                return [nums.index(n), ls.index(remain)+1]