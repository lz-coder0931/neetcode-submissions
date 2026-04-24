class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i, inter in enumerate(intervals):
            print(newInterval, inter)
            if inter[1]<newInterval[0]:
                res.append(inter)
            elif inter[0]>newInterval[1]:
                res.append(newInterval)
                res = res+intervals[i:]
                return res
            else:
                newInterval = [min(newInterval[0], inter[0]), max(newInterval[1], inter[1])]
                print(newInterval)
        res.append(newInterval)

        return res