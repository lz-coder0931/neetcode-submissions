class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force
        res = 0
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)):
                res = max(prices[j]-prices[i],res)

        return res
        