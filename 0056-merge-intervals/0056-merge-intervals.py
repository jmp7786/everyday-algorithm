class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []
        n = len(intervals)
        idx = 1
        while idx < n:
            start, end = intervals[idx-1]
            iidx = idx
            while iidx < n and end >=  intervals[iidx][0]: 
                start = min(start, intervals[iidx][0])
                end = max(end, intervals[iidx][1])
                iidx += 1
            result.append([start, end])
            # if iidx > idx:
            idx = iidx
            # else:
            idx +=1
            print(idx)
        
        if not result or max(intervals, key= lambda x: x[1])[1] != result[-1][1]: 
            result.append(intervals[-1])
        return result
