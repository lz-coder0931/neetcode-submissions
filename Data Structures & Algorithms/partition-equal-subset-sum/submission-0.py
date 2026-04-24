class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums)%2:
            return False
        
        target = sum(nums)/2

        dp = set()
        dp.add(0)
        for n in nums:
            nextdp = dp.copy()
            for t in dp:
                if t+n not in nextdp:
                    nextdp.add(t+n) 
                    
            dp = nextdp

        return True if target in dp else False
        