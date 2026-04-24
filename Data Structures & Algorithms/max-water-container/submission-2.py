class Solution:
    def maxArea(self, heights: List[int]) -> int:

        largest = 0
        ans = 0

        for i in range(len(heights)):
            for j in range(len(heights)-1, -1, -1):
                largest = min(heights[i], heights[j]) * (j-i)
                ans = max(ans, largest)
                if i > j:
                    break
        
        return ans



        