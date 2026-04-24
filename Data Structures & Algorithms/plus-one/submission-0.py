class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        m = len(digits)
        res = 0
        output = []
        for i in range(m):
            res = res+digits[i]*(10**(m-i-1))
        res = str(res+1)
        for i in range(len(res)):
            output.append(res[i])
        return output