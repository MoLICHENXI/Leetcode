#两种解法


#暴力解法
#即 只要看到数组中有大于等于target的值那么就直接返回当前的位置 i。(大于就意味着插入的值填在这个地方)
#如果循环了一遍都没找到 就证明该值填入数组最后一位 就是len(nums)位置处


#解法一
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        flag = 0
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
'''


#解法二
#用二分查找的方式 找到目标值的位置 返回start或ends + 1(因为没有找到的时候 结束条件一定是 start = ends + 1)
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left)//2
            if nums[mid]  == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
        return left
'''