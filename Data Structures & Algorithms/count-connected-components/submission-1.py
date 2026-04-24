class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjmap = {i:[] for i in range(n)}

        for a,b in edges:
            adjmap[a].append(b)
            adjmap[b].append(a)
        
        res = 0
        visit = set()
        cur = set()
        q = deque()


        for i in range(n):            
            if i not in visit:
                q.append(i)
                visit.add(i)
                cur.add(i)
                while q:
                    v = q.popleft()
                    for nei in adjmap[v]:
                        if nei not in cur:
                            visit.add(nei)
                            cur.add(nei)
                            q.append(nei)
                
                res += 1
                cur.clear()
        
        return res



