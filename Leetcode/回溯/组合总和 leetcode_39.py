class Solution:
    def combinationSum(self, candidates, target):
        if not candidates:
            return []

        result = []
        path = []
        def backtracking(candidates, targetsum, target, startindex):
            if targetsum > target:
                return
            if targetsum == target:
                result.append(path[:])
                return

            for i in range(startindex, len(candidates)):
                targetsum += candidates[i]
                path.append(candidates[i])
                #注意 这里startindex不需要i+1 因为可以选择重复值，因此如果candidate = [2,3,5]，那么从2开始可以选择[2,3,5]；从3开始可以选择[3,5]等
                backtracking(candidates, targetsum, target, i)
                targetsum -= candidates[i]
                path.pop()

        backtracking(candidates, 0, target, 0)
        return result

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        result = []
        path = []

        # 要剪枝的话必须先排序
        candidates.sort()
        def backtracking(candidates, targetsum, target, startindex):
            if targetsum > target:
                return
            if targetsum == target:
                result.append(path[:])
                return

            for i in range(startindex, len(candidates)):
                #如果当前的sum + 即将相加的candidates[i]已经大于target 那就没有意义了 直接返回
                if targetsum + candidates[i] > target:
                    return
                targetsum += candidates[i]
                path.append(candidates[i])
                backtracking(candidates, targetsum, target, i)
                targetsum -= candidates[i]
                path.pop()

        backtracking(candidates, 0, target, 0)
        return result

X = Solution()
print(X.combinationSum( [2,3,5],8))

