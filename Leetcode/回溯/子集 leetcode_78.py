class Solution:
    #利用递归的思想解题 不需要回溯
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in range(0,len(nums)):
            for j in res[:]:
                res.append(j + [nums[i]])
        return res


    #使用了回溯，收集每个节点的集合
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        result = []
        path = []

        def backtracking(nums, startindex):
            #先收集
            result.append(path[:])
            #到达叶子结点就回溯
            if startindex == len(nums):
                return
            for i in range(startindex, len(nums)):
                path.append(nums[i])
                backtracking(nums, i + 1)
                path.pop()

        backtracking(nums, 0)
        return result