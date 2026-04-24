class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        inilen = len(t)
        if len(s) != len(t):
            return False
        else:
            for n in s:
                inilen = len(t)
                for m in t:
                    if n == m:
                        t = t.replace(m, '', 1)
                        s = s.replace(n, '', 1)
                        if len(s) == 0:
                            return True
                        else:
                            break
                    elif len(t) == 1:
                        return False
                if len(t) == inilen:
                    return False

