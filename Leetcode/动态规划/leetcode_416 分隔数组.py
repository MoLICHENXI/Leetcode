class Solution:
    def canPartition(self, nums):
        # 先套上背包问题，这是个01背包问题，dp数组使用1维的滚动数组，按照前文的分析从后向前遍历
        # dp数组的含义是当前大小的背包能装进的最大重量，而本题中，背包大小为sum(nums)/2
        if sum(nums) % 2 == 1:
            return False
        # 创建一个一维数组
        dp = [0] * (sum(nums) // 2 + 1)
        for i in range(0, len(nums)):
            for j in range(len(dp), -1, -1):
                if j >= nums[i]:
                    dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
                # if dp[-1] == len(dp) - 1:
        print(dp)


if __name__ == '__main__':
    X = Solution()
    X.canPartition([1, 2, 5])