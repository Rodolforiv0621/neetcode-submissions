"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True
        intervals.sort(key = lambda x: x.start)
        lastEnd = intervals[0].end
        lastStart = intervals[0].start
        for inter in intervals:
            print(inter.start, inter.end)
        for meeting in intervals[1:]:
            end = meeting.end
            start = meeting.start
            if start < lastEnd:
                return False
            lastEnd = end
            

        return True