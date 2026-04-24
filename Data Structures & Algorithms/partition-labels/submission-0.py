class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        visit = defaultdict()
        res = []

        for i, ch in enumerate(s):
            if ch not in visit:
                visit[ch] = i
                res.append(1)
            else:
                ind = visit[ch]
                cnt= 0
                for j, r in enumerate(res):
                    if r+cnt<ind+1:
                        cnt = cnt+r
                        continue
                    res[j:] = [sum(res[j:])+1]
            print(res)
            
        return res
