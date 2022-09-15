class Solution:
    def findMinArrowShots(self, points) -> int:
        #按照每个范围的开头进行排序
        if len(points) == 0:
            return 0
        points.sort(key=lambda x: x[0])
        result = 1
        for i in range(1, len(points)):
            if points[i][0] > points[i - 1][1]:  # 气球i和气球i-1不挨着，注意这里不是>=
                result += 1
            else:
                points[i][1] = min(points[i - 1][1], points[i][1])  # 更新重叠气球最小右边界
        return result

X = Solution()
print(X.findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))