class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        l = 0
        chardict = {}

        for r, c in enumerate(s):
            chardict[c] = 1 + chardict.get(c, 0)
            if (r - l + 1) - max(chardict.values()) > k:
                
                chardict[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans





        