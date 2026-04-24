class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i, T in enumerate(temperatures):
            while stack and T > stack[-1][0]:
                stacktemp, stacki = stack.pop()
                res[stacki] = i-stacki

            stack.append([T, i])
        return res