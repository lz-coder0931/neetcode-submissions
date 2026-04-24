class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        c1, c2 = 0, 0
        for i in range(2, len(cost)+1):
            temp = c2
            c2 = min(c1+cost[i-2], c2+cost[i-1])
            c1 = temp
        return c2
