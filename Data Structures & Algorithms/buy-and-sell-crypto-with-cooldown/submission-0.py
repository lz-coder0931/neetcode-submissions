class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        hold = -prices[0]
        sold, rest = 0,0

        for i in range(1, len(prices)):
            prev_sold = sold
            hold = max(hold, rest-prices[i])
            sold = max(sold, hold+prices[i])

            rest = prev_sold
        return sold



        