"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        
        # Extract start and end times
        start_times = sorted([interval.start for interval in intervals])
        end_times = sorted([interval.end for interval in intervals])
        
        start_pointer = 0
        end_pointer = 0
        num_rooms = 0
        max_rooms = 0
        
        while start_pointer < len(intervals):
            if start_times[start_pointer] < end_times[end_pointer]:
                num_rooms += 1
                start_pointer += 1
            else:
                num_rooms -= 1
                end_pointer += 1
            max_rooms = max(max_rooms, num_rooms)
        
        return max_rooms