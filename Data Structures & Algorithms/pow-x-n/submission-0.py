class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        neg = False
        res = 1
        if n == 0:
            return res
        if n<0:
            neg = True
            n = -n
        for i in range(n):
            res *= x

        if neg:
            res = 1/res
        return res 
