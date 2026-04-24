import math
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minimal = float('inf')

        return self.binarysearch(nums, left, right, minimal)

    def binarysearch(self, nums, left, right, minimal):
        print(left, right, minimal)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid+1
            else:
                right = mid-1
            minimal = min(minimal, nums[mid])
            print(left, right, mid, minimal)
            return self.binarysearch(nums, left, right, minimal)
        return min(minimal, nums[left])



    # start+1 < end 
    # // flooring

            # while (left) < right:
            # if nums[math.ceil((left+right) / 2)] < minimal:
            #     minimal = nums[math.ceil((left+right) / 2)]
            #     left = left
            #     right = math.ceil((left+right) / 2)
            # else:
            #     left = math.ceil((left+right) / 2)
            #     right = right
            #     minimal = minimal