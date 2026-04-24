class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        freqdict = {}
        for i, n in enumerate(nums):
            freqdict[n] = 1 + freqdict.get(n, 0)
        # print(sorted(freqdict))
        for w in sorted(freqdict, key = freqdict.get, reverse=True):
            ans.append(w)
            if len(ans) == k:
                return ans