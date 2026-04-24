class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        while l<=r:
            mid = l+(r-l)//2
            ht = 0
            for p in piles:
                ht += (p+mid-1)//mid
            if ht>h:
                l = mid+1
            else:
                if mid == 1:
                    return mid
                hv = 0
                for p in piles:
                    hv += (p+mid-2)//(mid-1)
                if hv>h:
                    return mid
                else:
                    r = mid-1
        