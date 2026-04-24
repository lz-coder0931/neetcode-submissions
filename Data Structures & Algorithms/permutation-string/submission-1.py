class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_map = {}
        for char in s1:
            freq_map[char] = freq_map.get(char, 0)+1

        l, r = 0, len(s1)-1
        while r < len(s2):
            map_copy = freq_map.copy()
            for r_i in range(r, r - len(s1), -1):
                if map_copy.get(s2[r_i],0) > 0:
                    map_copy[s2[r_i]] -=1
                    if r_i == r - len(s1)+1:
                        return True

                else:
                    l = r_i + 1
                    r = l + len(s1)-1
                    break
        return False

# I tried to apply boyer here(works for skipping), but since we need to 
# recount the moving window, which means its O(M) so total is O(M*N), however, 
# we can simply maintain the silde window dict, compare 2 dict directly.

