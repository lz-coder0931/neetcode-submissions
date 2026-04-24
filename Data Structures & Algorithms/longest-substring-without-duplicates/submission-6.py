class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l,r = 0,0
        charSet = set()
        while r < len(s):
            if s[r] in charSet:
                while s[l] != s[r]:
                    charSet.remove(s[l])
                    l += 1
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r-l+1)
            r +=1

        return res


