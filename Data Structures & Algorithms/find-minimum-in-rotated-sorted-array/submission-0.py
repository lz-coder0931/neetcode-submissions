class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] <= nums[-1]:
            return nums[0]
        else:
            left = 0 
            right = len(nums) - 1
            minimal = nums[-1]
            while (left+1) < right:
                if nums[(left+right) // 2] < minimal:
                    minimal = nums[(left+right) // 2]
                    left = left
                    right = (left+right) // 2
                    
                else:
                    left = (left+right) // 2
                    right = right
                    minimal = minimal

                print(minimal, left, right)
            
            return minimal

    # def binarysearch(self, nums, left, right, minimal):



        