class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_map = {}
        check_map = {}
        for char in s1:
            freq_map[char] = freq_map.get(char,0)+1
        for char in s2[:len(s1)]:
            check_map[char] = check_map.get(char, 0) +1
        if freq_map == check_map:
            return True

        for r in range(len(s1),len(s2)):
            check_map[s2[r]] = check_map.get(s2[r], 0) + 1
            check_map[s2[r-len(s1)]] = check_map.get(s2[r-len(s1)],0) - 1
            print(check_map)
            if check_map[s2[r-len(s1)]] == 0:
                del check_map[s2[r-len(s1)]]
            if freq_map == check_map:
                return True

        return False
            
