## We need to process in increasing start times, when no meeting room, we allowcate a first meeting room. And second comes in, as first is not finished, we add another meeting room => an effective storing method is to keep the end time as the key, earlist first, if top is not free, then no one does -> add new room

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        end_time = []
        for interval in intervals:
            if end_time != [] and interval[0] >= end_time[0]:
                end_time[0] = interval[1]
                end_time.sort()
            else: 
                end_time.append(interval[1])
                end_time.sort()
                    
        return len(end_time)
