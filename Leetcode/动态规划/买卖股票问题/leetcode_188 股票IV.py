class Solution:
    def maxProfit(self, k: int, prices) -> int:
        # 如果按照第123题的思路，那么这道题也可以完成，时间复杂度为O(n)，空间复杂度O(k)
        # 那么一共有2 * k + 1种状态

        # 直接写并完成初始化
        dp = [[0] * (2*k + 1) for i in range(len(prices))]

        # 奇数次的初始化都是- prices[0],偶数次的初始化都是0
        for i in range(2*k + 1):
            if i % 2 == 1:
                dp[0][i] = - prices[0]

        #遍历形式从上到下从左至右，每次都是找左上角的位置
        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                if j % 2 == 1:
                    #该状态为持有股票的状态
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i])
                else:
                    #该状态为不持有股票的状态
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + prices[i])
        return dp[-1][-1]

if __name__ == "__main__":
    X = Solution()
    print(X.maxProfit(k = 2, prices = [3,2,6,5,0,3]))