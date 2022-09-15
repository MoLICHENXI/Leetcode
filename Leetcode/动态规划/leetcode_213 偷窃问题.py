class Solution:
    def rob(self, nums) -> int:
        # 因为是一圈 因此第一个和最后一个不能同时选择
        # 所以遍历两遍 选择最大值即可
        # dp[j]还是代表当前能偷的最大值

        # 可以简化一下
        if len(nums) < 3:
            return max(nums)

        prev = nums[0]
        curr = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            prev, curr = curr, max(prev + nums[i], curr)

        prev1 = nums[1]
        curr1 = max(nums[1], nums[2])
        for i in range(3, len(nums)):
            prev1, curr1 = curr1, max(prev1 + nums[i], curr1)

        return max(curr, curr1)

if __name__ == '__main__':
    X = Solution()
    print(X.rob([200,3,140,20,10]))