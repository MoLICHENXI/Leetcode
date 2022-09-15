#删除重复元素 只保留一位
#使用快慢指针进行求解

class Solution:
    def removeDuplicates(self, nums: [int]) -> int:
        slow = 0
        fast = 0
        for fast in range(len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1

X=Solution()
print(X.removeDuplicates([1,1,2,3]))