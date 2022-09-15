class Solution:
    def findTargetSumWays(self, nums, target):
        # 先写个二维数组
        # 根据left - right = target，right = sum -left，就有left= (target + sum)//2，即背包容量就是left，有几种方法能填满
        # 那么二维数组的大小就是dp[i][j] len(nums) * ((sum + target)//2 + 1) 其中dp[i][j]表示第i个数在容量为j的背包中有几种方法
        # 初始化是说，我们对所有dp[i][0]都初始化为1，并且对dp[0][j]的唯一一位做初始化
        # 递推公式是说我们选择dp[i - 1][j - nums[i]]以及当前的dp[i - 1][j]放到当前的dp[i][j]上，遍历顺序从左至右即可
        if (target + sum(nums)) % 2 == 1:
            return 0
        if abs(target) > sum(nums):
            return 0

        # 创建二维数组dp
        dp = [[0 for i in range((sum(nums) + target) // 2 + 1)] for j in range(len(nums))]

        # 初始化dp

        dp[0][0] = 1

        for j in range(len(dp[0]) - 1, -1 , -1):
            if j >= nums[0]:
                dp[0][j] = dp[0][j] + dp[0][j - nums[0]]
        # 开始遍历
        for i in range(1, len(dp)):
            for j in range(0, len(dp[0])):
                dp[i][j] = dp[i - 1][j - nums[i]] + dp[i - 1][j] if j >= nums[i] else dp[i - 1][j]
        return dp

        # if (target + sum(nums)) % 2 == 1:
        #     return 0
        # if abs(target) > sum(nums):
        #     return 0
        #
        #     # 创建一个一维数组
        # dp = [0] * ((sum(nums) + target) // 2 + 1)
        #
        # # 初始化
        # dp[0] = 1
        #
        # # 开始遍历
        # for i in range(len(nums)):
        #     for j in range(len(dp) - 1, -1, -1):
        #         if j >= nums[i]:
        #             dp[j] += dp[j - nums[i]]
        #         else:
        #             dp[j] = dp[j]
        # return dp

if __name__ == '__main__':
    X = Solution()
    print(X.findTargetSumWays([1,1,1,1,1],3))