class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqmap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preqmap[crs].append(pre)
        
        visit = set()
        def dfs(crs):

            if crs in visit:
                return False
            if preqmap[crs] == []:
                return True
            
            visit.add(crs)
            for c in preqmap[crs]:
                if not dfs(c):
                    return False
            visit.remove(crs)
            preqmap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True