#双指针求三数之和



class Solution:
    def threeSum(self, nums):
        result = list()   #存储结果的数组
        nums.sort()       #先排序

        if len(nums) < 3 or nums[0] > 0:
            return result

        i = 0
        for i in range(len(nums)):
            right = len(nums) - 1
            target = - nums[i]                                       #要找到的目标值
            if i > 0 and nums[i] == nums[i -1]:                      #有相同元素就往后查找
                continue
            for left in range(i + 1,len(nums)):                      #始终在i的右边开始
                if left > i + 1 and nums[left] == nums[left - 1]:    #有相同元素就向右移动
                   continue
                while left < right and nums[left] + nums[right] > target:
                    right -= 1
                if left == right:
                    break
                elif nums[left] + nums[right] == target:
                    result.append([nums[i],nums[left],nums[right]])
        return result

X = Solution()
print(X.threeSum([-1,0,1,2,-1,-4]))