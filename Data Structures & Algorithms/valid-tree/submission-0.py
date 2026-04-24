class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        gmap = {i:[] for i in range(n)}
        for a,b in edges:
            gmap[a].append(b)
            gmap[b].append(a)

        visit = set()
        def dfs(node,pre):
            for v in gmap[node]:
                if v == pre:
                    continue
                if v in visit:
                    return False
                visit.add(v)
                if not dfs(v, node):
                    return False
            return True
        visit.add(0)
        return dfs(0,-1) and n==len(visit)