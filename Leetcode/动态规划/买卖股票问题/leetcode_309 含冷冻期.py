class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 1:
            return 0
        # 这道题目加入了冷冻期这个概念 也就是说冷冻期是要暂停一天操作的
        # 因此还是找一个dp[i][j]表示第i天第j个状态的最大利润
        # 那么本道题中，j一共四种状态，状态0：持有股票的状态；而不持有股票的状态又分为两种，一种是状态1：今天卖出了股票
        # 另一种状态2：两天及以前就卖出了股票，也就是度过了一天的冷冻期，现在还保持不持有股票的状态
        # 最后一种状态3：今天是冷冻期，不操作

        # 递推公式，因为dp[i][0]代表第i天持有股票，因此dp[i][0]就是两种情况，第一种，之前已经持有了股票；
        # 第二种，今天刚买入股票，那么这里也分为两种情况，前一天的状态是冷冻期或者前一天是一直保持卖出的状态
        # 即dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][3] - prices[i], dp[i - 1][2] - prices[i]))

        # dp[i][1] 代表第i天在今天卖出了股票，即dp[i][1] = dp[i - 1][0] + prices[i]
        # dp[i][2] 代表在第i天的两天及以前就卖出了股票,即前一天可能一直是第一个状态，也可能是冷冻期
        # 则dp[i][2] = max(dp[i - 1][2], dp[i - 1][3])
        # dp[i][3]因为是冷冻期，因此dp[i][3] = dp[i - 1][1]

        # 初始化部分
        dp = [[0] * 4 for i in range(len(prices))]
        dp[0][0] = -prices[0]

        # 遍历顺序从上到下从左至右
        for i in range(1, len(dp)):
            dp[i][0] = max(dp[i - 1][0], max(dp[i - 1][3] - prices[i], dp[i - 1][2] - prices[i]))
            dp[i][1] = dp[i - 1][0] + prices[i]
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][3])
            dp[i][3] = dp[i - 1][1]

        # 返回不持有股票的三种状态的最大值
        return max(dp[-1][-1], dp[-1][-2], dp[-1][-3])

if __name__ == "__main__":
    X = Solution()
    print(X.maxProfit(prices = [1,2,3,0,2]))