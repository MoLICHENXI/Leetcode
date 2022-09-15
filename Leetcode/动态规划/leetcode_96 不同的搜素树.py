class Solution:
    def numTrees(self, n) -> int:
        # 1、先明确dp的含义，就是当前n个节点的二叉搜索树个数
        # 2、找到递推公式 根据根节点来找到对应关系

        # 创建dp数组
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        # 初始化 dp[0] = 1 dp[1] = 1
        # 递推公式，并且从左至右遍历
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[i - j] * dp[j - 1]
        return dp

X = Solution()
print(X.numTrees(5))