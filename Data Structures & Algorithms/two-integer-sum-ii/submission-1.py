class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r =0, len(numbers)-1
        while r > l:
            if numbers[l] < target-numbers[r]:
                l+=1
            if numbers[l] > target-numbers[r]:
                r -=1
            if numbers[l] == target -numbers[r]:
                return [l+1, r+1]