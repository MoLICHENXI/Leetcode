class Solution:
    def combinationSum2(self, candidates, target: int):
        if not candidates:
            return []

        result = []
        path = []

        # 这里需要对同一个树层里使用过的数进行去重
        # used = [0]*len(candidates)

        candidates.sort()

        def backtracking(candidates, startindex, targetsum, target):
            if targetsum == target:
                result.append(path[:])
                return

            for i in range(startindex, len(candidates)):
                # 先做去重,在candidates[i]和candidates[i- 1]相同的情况下，used数组的前一位为0表示前一位没用过，即
                # 当前不是纵向相同，而是横向的层相同，这时就要去重，直接continue跳过即可

                if i > startindex and candidates[i] == candidates[i - 1]:
                    continue
                # 这里做剪枝操作，直接进行返回
                if targetsum + candidates[i] > target:
                    return

                targetsum += candidates[i]
                # 这里对used数组进行修改
                # used[i] = 1
                path.append(candidates[i])
                backtracking(candidates, i + 1, targetsum, target)
                path.pop()
                # used[i] = 0
                targetsum -= candidates[i]

        backtracking(candidates, 0, 0, target)
        return result

X = Solution()
print(X.combinationSum2(candidates = [2,5,2,1,2], target = 5))