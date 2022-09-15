class Solution:
    def change(self, amount: int, coins):
        # 这是完全背包问题
        # dp[i][j]代表第i个金额在总金额为j的最多组合数

        #二维的递推公式是，dp[i][j] += dp[i][j - coins[i]] + dp[i - 1][j] if j >= coins[i]；这句话的意思是如果当前的总金额大于等于目前的硬币 那么一种来源是在之前总金额为j-coins[i]的部分方法
        #另一种来源是，没加这个硬币，即coins[i - 1]的时候，对应的总金额j的方法，这两个方法数量相加就是目前的总方法
        #如果j < coins[i]，那就是dp[i][j]把上一位的dp[i - 1][j]继承过来即可

        # 初始化一个二维数组
        dp = [[0 for i in range(amount + 1)] for j in range(len(coins))]

        # 什么都不放，总金额为0，也有一种方法
        dp[0][0] = 1

        # 先初始化第一行的内容
        for j in range(len(dp[0])):
            if j >= coins[0]:
                dp[0][j] += dp[0][j - coins[0]]

        for i in range(1, len(dp)):
            for j in range(0, len(dp[0])):
                # 每一行的第一个都是初始化为1
                if j == 0:
                    dp[i][j] = 1
                elif j >= coins[i]:
                    dp[i][j] += dp[i][j - coins[i]] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[-1][-1]


if __name__ == '__main__':
    X = Solution()
    print(X.change(100,[1,101,102,103]))