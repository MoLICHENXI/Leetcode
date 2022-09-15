class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 存储最后的结果
        result = []
        # 存储中间的集合
        path = []

        def backtracking(startindex, n, k):
            # 返回条件
            if len(path) == k:
                # 处理节点并返回
                # !!!这里一定要注意，path 是会随着边的 所以需要改成path[:]
                result.append(path[:])
                return

            # 根据N叉树的思想，for循环的大小就是数组的长度n
            # 起始点是根据题目要求，保证不重复

            #可以选择进行剪枝
            for i in range(startindex, n - (k - len(path)) + 2):
            # for i in range(startindex, n + 1):
                # 把i先添加进去
                path.append(i)
                # 递归(N叉数)、从startindex + 1开始
                backtracking(i + 1, n, k)
                # 递归结束后，回溯，即把当前的path最后一个值删掉
                path.pop()

        backtracking(1, n, k)
        return result