class Solution:
    def integerBreak(self, n):
        # 1、首先 思路是 如果是4的话 因为4可以分为2*2 由于2的最大乘积是1，因此2*1*2*1
        # 2、同理，n = 3 可以分成1，2；乘积就是2 ；n = 5乘积最大化为6，因而就是2,3；n = 6的乘积最大化结果就是3，3 = 9；
        # 3、10可以拆分成5,5，5可以拆分成2,3;

        # dp数字的每个位置代表当前整数的最大成绩
        # 递推公式，dp[i] = dp[i//2]dp[i-i//2]
        # 初始化，dp[0] = 0 dp[1] = 0 dp[2] = 1 dp[3] = 2 dp[4] = 4 dp[5] = 6
        dp = [0] * 59
        dp[2] = 1
        dp[3] = 2
        # dp[4] = 4
        # dp[5] = 6
        if n <= 3:
            return dp[n]
        for i in range(4, n + 1):
            for j in range(2, i-1):
                dp[i] = max(j*dp[i-j], j*(i-j), dp[i])
        return dp
X = Solution()
print(X.integerBreak(58))