class Solution:
    def isMonotonic(self, nums):
        increase = False  #表示数组初始化 递增为false
        decrease = False  #表示数组初始化 递减为false
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                increase = True   #当前判断数据是递增趋势
            elif nums[i] > nums[i + 1]:
                decrease = True   #当前根据判断数据应该是递减趋势
            #如果最后数据是递增的 那么increase 是True decrease 是False
            #如果数据是递减的 那么increase和decrease同理
        return not (increase and decrease)

X= Solution()
print(X.isMonotonic([1,3,2]))