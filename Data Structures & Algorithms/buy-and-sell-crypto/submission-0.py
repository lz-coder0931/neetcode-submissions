class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices)-1):
            n = min(prices[0:i+1])
            m = max(prices[i+1:len(prices)])
            if m-n > profit:
                profit = m-n
        return profit


        