class Solution:
    def lastStoneWeightII(self, stones) -> int:
        # dp[i][j]代表当前第i个石头在容量为j的背包中最大的重量
        # 解决本题是需要尽量将两堆石头分成重量相等的两份，因此我可以找一个总和一半大小容量的背包，往里面放东西

        # 使用一个一维数组顺便直接初始化
        dp = [0] * (sum(stones) // 2 + 1)
        #倒序遍历，从右至左，先遍历物品后遍历容量
        for i in range(len(stones)):
            #注意j的初始值len(dp) - 1
            for j in range(len(dp) - 1, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        print(dp)

if __name__ == '__main__':
    X = Solution()
    X.lastStoneWeightII([2,7,4,1,8,1])