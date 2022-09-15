#长度最小的子数组
#使用滑动窗口解决，实际上是个双指针

class Solution:
    def minSubArrayLen(self, target: int, nums: [int]) -> int:
        total = 0
        length = float('inf')
        slow = 0
        for fast in range(len(nums)):
            total += nums[fast]     #求和阶段，只要sum小于target的时候就一直计算
            while total >= target:
                length = min(length,fast - slow + 1)
                total -= nums[slow]
                slow +=1
        return 0 if length == float('inf') else length


X = Solution()
print(X.minSubArrayLen(7,[2,3,1,2,4,3]))
