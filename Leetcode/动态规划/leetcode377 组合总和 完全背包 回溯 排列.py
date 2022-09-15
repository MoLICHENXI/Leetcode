# class Solution:
#     def combinationSum4(self, nums, target):
#         count = 0
#
#         def backtracking(nums, target, sum1):
#             nonlocal count
#             if sum1 >= target:
#                 if sum1 == target:
#                     count += 1
#                 return
#
#             for i in range(len(nums)):
#                 sum1 += nums[i]
#                 backtracking(nums, target, sum1)
#                 sum1 -= nums[i]
#
#         backtracking(nums, target, 0)
#         return count

class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        dp = [0 for i in range(target + 1)]
        dp[0] = 1

        for i in range(1, len(dp)):
            for j in range(0, len(nums)):
                if i >= nums[j]:
                    dp[i] += dp[i - nums[j]]
                else:
                    dp[i] = dp[i]
        return dp

if __name__ == '__main__':
    X = Solution()
    print(X.combinationSum4([1,2,3],4))