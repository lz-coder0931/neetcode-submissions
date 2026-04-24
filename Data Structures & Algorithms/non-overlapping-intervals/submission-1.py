class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = 0
        prevend = intervals[0][1]
        for inter in intervals[1:]:
            if prevend > inter[0]:
                res +=1
                prevend = min(prevend, inter[1])
            else:
                prevend = inter[1]
        return res
