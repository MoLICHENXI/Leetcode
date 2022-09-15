class Solution:
    def maxProfit(self, prices) -> int:
        # dp数组的意义在于确定每天在持有和不持有股票的两种情况下 拥有的最大利润
        # 其中dp[i][0]是说第i天持有股票能得到的最大利润，dp[i][1]是第i天不持有股票能得到的最大利润
        # dp[i][0] = max(dp[i - 1][0], -prices[i])这个是说当前第i天持有股票能获得的最大利润，是今年刚买入和昨天已经持有股票
        # 的最大值
        # dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] + prices[i])就是昨天不持有的情况和今天卖出(也是今天不持有)的两种情况

        # 初始化dp数组
        dp = [[0] * 2 for i in range(2)]
        dp[0][0] = - prices[0]  # 持有股票的初始化
        dp[0][1] = 0  # 不持有股票的初始化

        # 从上至下从左至右的遍历顺序
        for i in range(1, len(prices)):
            dp[i % 2][0] = max(dp[i % 2 - 1][0], -prices[i])
            dp[i % 2][1] = max(dp[i % 2 - 1][1], prices[i] + dp[i % 2 - 1][0])

        return dp[len(prices) % 2 - 1][-1]

if __name__ == '__main__':
    X = Solution()
    print(X.maxProfit([1,2,4]))