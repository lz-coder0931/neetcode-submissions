class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # if len(nums) == 1:
        #     R = nums[0]
        # elif len(nums) == 2:
        #     R = max(nums[0], nums[1])
        # else:
        #     r1, r2 = nums[0], nums[1]
        #     for i in range(2, len(nums)):               
        #         R = max(r2, r1+nums[i])
        #         r1 = r2
        #         r2 = R
        #         print(r1, r2, R)
        # return R
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
            print(rob1, rob2)
        return rob2
