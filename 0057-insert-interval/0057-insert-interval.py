class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: 
            return [newInterval]
        new_start, new_end = newInterval

        candidates = [] 
        for i in range(len(intervals)): 
            start, end = intervals[i]

            if new_end >= end and new_start <= end : 
                candidates.append(i)
                new_start = min(new_start, start)
            elif new_start <= start and new_end >= start:
                candidates.append(i)
                new_end = max(new_end, end)
            elif start<= new_start and new_end <=end: 
                candidates.append(i)
                new_start = min(new_start, start)
                new_end = max(new_end, end)
        
        merged_interval = [new_start, new_end]

        new_intervals = []
        inserted = False
        for i in range(len(intervals)): 
            if i not in candidates:
                new_intervals.append(intervals[i])
            elif not inserted: 
                inserted= True
                new_intervals.append(merged_interval)
        # merge는 되지 않고 interval만 있을 경우                 
        if not inserted:
            intervals.append(newInterval)
            intervals.sort()
            new_intervals = intervals
        return new_intervals
