class Solution:

    def encode(self, strs: List[str]) -> str:
        enstr = ''
        for s in strs:
            enstr = enstr + str(len(s))
            enstr = enstr + '#'
            enstr = enstr + s
        return enstr

    def decode(self, s: str) -> List[str]:
        ls = []
        l = 0
        r = 0
        while r < len(s):
            
            if s[r] == '#':
                n = int(s[l:r])
                ls.append(s[r+1:r+n+1])
                l = r+n+1
                if l >= len(s):
                    break
                r = l + 1
            else:
                r = r+1
        
        return ls



