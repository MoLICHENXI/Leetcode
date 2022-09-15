class Solution:
    def maxProfit(self, prices) -> int:
        # 因为最多能完成两笔交易，因此一共有五种状态
        # 状态0：不操作 状态1：第一次买入 状态2：第一次卖出 状态3：第二次买入 状态4：第二次卖出
        # 因此dp数组的意义在于dp[i][j]表示第i天第j个状态的最大利润值

        # 递推公式，因为第一次持有股票的状态就是，dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])，即当天买入股票
        # 或前面已经买入了股票

        # 第一次不持有股票的状态就是，dp[i][2] = max(dp[i - 1][1] + prices[i], dp[i - 1][2])，即当天卖出或前面已经卖出
        # 同理，第二次持有股票的状态就是，dp[i][3] = max(dp[i - 1][2] - prices[i], dp[i - 1][3])
        # 第二次不持有股票的状态就是，dp[i][4] = max(dp[i - 1][3] + prices[i], dp[i - 1][4])
        # 因为最大值应该出现在第二次买卖股票后，所以返回值就直接是dp[-1][4]

        # 第三部分是准备初始化的部分，因为可以看到所有递推公式都是有前面一种状态推导出来的
        # 因此dp[0][0] = 0对应于不操作
        # dp[0][1] = -prices[0] 对应于第一次买入
        # dp[0][2] = 0 对应于第一次卖出，相当于不持有股票
        # dp[0][3] = -prices[0]对应于第二次买入
        # dp[0][4] = 0对应于第二次卖出，相当于也不持有股票

        #初始化数组
        dp = [[0] * 5 for i in range(len(prices))]
        dp[0][1] = -prices[0]
        dp[0][2] = 0
        dp[0][3] = -prices[0]
        dp[0][4] = 0

        #因为在得到一个新的dp[i][j]时，需要知道左上方的值，因此遍历顺序从左至右，从上至下
        for i in range(1, len(dp)):
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
            dp[i][2] = max(dp[i - 1][1] + prices[i], dp[i - 1][2])
            dp[i][3] = max(dp[i - 1][2] - prices[i], dp[i - 1][3])
            dp[i][4] = max(dp[i - 1][3] + prices[i], dp[i - 1][4])
        return dp[-1][4]

if __name__ == '__main__':
    X = Solution()
    print(X.maxProfit([3,3,5,0,0,3,1,4]))