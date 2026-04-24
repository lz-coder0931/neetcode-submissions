class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        gmap={i: [] for i in range(1,len(edges)+1)}
        for a,b in edges:
            gmap[a].append(b)
            gmap[b].append(a)

        visit = set()
        sub = set()
        prev = 0
        cyclestart = -1
        def dfs(cur, prev):
            nonlocal cyclestart
            for nei in gmap[cur]:
                print(nei)
                if nei == prev:
                    continue
                if nei in visit:
                    cyclestart = nei
                    return True
                visit.add(nei)
                if dfs(nei,cur):
                    if cyclestart != -1:
                        sub.add(nei)
                    if cyclestart == nei:
                        sub.add(nei)
                        cyclestart = -1
                    return True
            return False

        
        dfs(1, prev)

        for u,v in reversed(edges):
            if u in sub and v in sub:
                return [u,v]
        return [1,2]




