class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []
        def btrack(i, remain):
            if len(remain)==0:
                res.append(sub.copy())
                return
            for j in range(0, len(remain)):
                sub.append(remain[j])
                tmp = remain.pop(j)
                btrack(j+1, remain)
                sub.pop()
                remain.insert(j,tmp)

        btrack(0, nums)
        return res