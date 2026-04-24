class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        tab = [False] *(len(s)+1)
        tab[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if tab[j] and s[j:i] in wordDict:
                    tab[i] = True
                    break

        return tab[-1]


        