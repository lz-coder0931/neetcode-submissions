"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        res = 0
        intervals.sort(key=lambda i: i.start)
        dayEnd = []
        if not intervals:
            return 0
        dayEnd.append(intervals[0].end)
        for inter in intervals[1:]:
            for i, de in enumerate(dayEnd):
                print(dayEnd)
                if inter.start>=de:
                    dayEnd[i] = inter.end
                    break
                elif i == len(dayEnd)-1:
                    dayEnd.append(inter.end)
                    break
        return len(dayEnd)
