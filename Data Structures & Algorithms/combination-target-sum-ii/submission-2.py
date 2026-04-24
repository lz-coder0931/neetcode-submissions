class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        added = set()
        candidates.sort()
        def btrack(i):
            if sum(sub) == target:
                if tuple(sub) not in added:
                    added.add(tuple(sub.copy()))
                    res.append(sub.copy())
                return
            if i==len(candidates) or sum(sub) > target:
                return
            sub.append(candidates[i])
            btrack(i+1)
            sub.pop()
            btrack(i+1)
        btrack(0)
        return res