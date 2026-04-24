class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        tab = [False] *(len(s)+1)
        tab[0] = True
        for i in range(1, len(s)+1):
            for j in range(i):
                if tab[j] and s[j:i] in wordDict:
                    tab[i] = True
                    break

        return tab[len(s)]
                # Using a set for O(1) average time complexity lookups
        # word_set = set(wordDict)
        
        # # dp[i] is True if s[:i] can be segmented
        # dp = [False] * (len(s) + 1)
        # dp[0] = True  # Base case for the empty string

        # # Iterate through the string to fill the DP table
        # for i in range(1, len(s) + 1):
        #     # Check all possible split points j before i
        #     for j in range(i):
        #         # If s[:j] is breakable AND s[j:i] is a word in the dictionary
        #         if dp[j] and s[j:i] in word_set:
        #             dp[i] = True
        #             break # Found a valid break for s[:i], no need to check other j's

        # # The last value tells if the whole string is breakable
        # return dp[len(s)]


        