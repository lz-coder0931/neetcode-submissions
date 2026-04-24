"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda inter: inter.start)
        if not intervals:
            return True

        prevend = intervals[0].end
        for inter in intervals[1:]:
            if prevend > inter.start:
                return False
            else:
                prevend = inter.end
        
        return True
