class Solution:
    def findSubsequences(self, nums):
        if not nums:
            return []

        result = []
        path = []

        def backtracking(nums, startindex):
            if len(path) >= 2:
                result.append(path[:])

            # 如果不能排序，就用集合记录重复值
            used = set()
            for i in range(startindex, len(nums)):
                # 判断递增序列
                if (path and nums[i] - path[-1] < 0) or nums[i] in used:
                    continue
                path.append(nums[i])
                used.add(nums[i])
                backtracking(nums, i + 1)
                path.pop()

        backtracking(nums, 0)
        return result

if __name__ == '__main__':
    X = Solution()
    print((X.findSubsequences([1,2,3,2,1])))