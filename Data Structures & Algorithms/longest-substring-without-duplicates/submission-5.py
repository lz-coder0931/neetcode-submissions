class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        repeatdict = {}
        ans = 0
        i = 0
        j = 0
        
        for k, c in enumerate(s):
            if c not in repeatdict:
                repeatdict[c] = repeatdict.get(c, k)
                j = k
                if j-i+1 > ans:
                    ans = j-i+1
            else:
                if repeatdict.get(c) < i:
                    repeatdict[c] = k
                    if k - i + 1 > ans:
                        ans = k - i + 1
                else:
                    i = repeatdict.get(c) + 1
                    repeatdict[c] = k
        return ans


