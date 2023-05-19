class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)

        ans = []
        n = len(intervals)-1
        i = 0
        while i<n:
            if intervals[i][1] >= intervals[i+1][0]:
                if intervals[i+1][1] > intervals[i][1]:
                    intervals[i][1] = intervals[i+1][1]
                intervals.remove(intervals[i+1])
                n-=1
                i-=1
            i+=1

        return intervals
