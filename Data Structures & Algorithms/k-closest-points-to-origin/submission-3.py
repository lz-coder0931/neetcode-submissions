class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        d = []
        for x, y in points:
            distance = -x**2-y**2
            heapq.heappush(d, [distance, x, y])
            if len(d)>k:
                heapq.heappop(d)

        res = []
        while d:
            dis, x, y = heapq.heappop(d)
            res.append([x,y])

        return res
        