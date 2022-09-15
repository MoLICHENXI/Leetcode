class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        res = []
        max_range_edge = intervals[0][1]
        start = intervals[0][0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= max_range_edge:
                #选最大的右边界
                max_range_edge = max(max_range_edge, intervals[i][1])
            else:
                res.append([start, max_range_edge])
                start = intervals[i][0]
                max_range_edge = intervals[i][1]
        res.append([start, max_range_edge])
        return res
X = Solution()
print(X.merge([[1,3],[2,6],[8,10],[15,18]]))