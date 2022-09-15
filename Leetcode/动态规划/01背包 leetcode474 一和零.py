from collections import defaultdict
class Solution:
    def findMaxForm(self, strs, m, n):
        # 这道题目前想到用二维数组
        # dp[i][j]代表i个0，j个1最大的子集长度
        # 递推公式是 (dp[i - nums(0)][j - nums(1)] + 1, dp[i][j]) 其中nums(0)是说第i个数中，0的个数
        # 初始化为全0
        # dp数组大小为 (m + 1) * (n + 1)

        # 创建dp数组
        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

        # 创建一个统计0， 1字符数量的函数
        def countnums(str1):
            d = defaultdict(int)
            for i in str1:
                d[i] += 1
            return d['0'], d['1']

        # 遍历顺序为每一个元素遍历一次，每次从上至下，从左至右遍历
        for k in strs:
            # count0, count1代表每次统计的0， 1个数
            count0, count1 = countnums(k)
            for i in range(len(dp) - 1, -1, -1):
                for j in range(len(dp[0]) -1 , -1, -1):
                    if j >= count0 and i >= count1:
                        dp[i][j] = max(dp[i - count1][j - count0] + 1, dp[i][j])
                    else:
                        dp[i][j] = dp[i][j]
        return dp

if __name__ == '__main__':
    X = Solution()
    print(X.findMaxForm(strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3))
