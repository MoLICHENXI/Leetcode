class Solution:
    def largestSumAfterKNegations(self, nums, k: int) -> int:
        #先从大到小排序
        nums.sort(key = lambda x : abs(x), reverse = True)
        for i in range(len(nums) - 1):
            if nums[i] <= 0:
                nums[i] = - nums[i]
                k -= 1
            if k ==0:
                break
        #如果退出了循环K还大于0
        while k > 0:
            nums[len(nums) - 1] = - nums[len(nums) - 1]
            k -= 1
        return sum(nums)
X= Solution()
print(X.largestSumAfterKNegations(nums = [4,2,3], k = 1))