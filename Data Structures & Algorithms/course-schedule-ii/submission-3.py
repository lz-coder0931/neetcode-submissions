class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        

        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        res = []

        visit = set()
        added = set()
        def dfs(crs):
            if crs in added:
                added.add(crs)
                return True
            if crs in visit:
                return False

            visit.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            preMap[crs] = []
            res.append(crs)
            added.add(crs)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
            
        
