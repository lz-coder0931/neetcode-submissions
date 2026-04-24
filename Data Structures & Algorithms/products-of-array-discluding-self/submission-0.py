class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        ls = []
        if 0 not in nums:
            for n in nums:
                prod = prod*n
            for i in range(len(nums)):
                ls.append(int(prod/nums[i]))
        else:
            for j, m in enumerate(nums):
                if m != 0:
                    ls.append(int(0))
                else:
                    temp = 1
                    for i , n in enumerate(nums):
                        if i != j:
                            temp = temp * n
                    ls.append(int(temp))
        return ls

        
        