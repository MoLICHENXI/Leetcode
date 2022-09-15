#查找峰顶位置

#根据二分法，峰顶可以将数组分成单调递增和单调递减的部分
#我们可以选择将单调递增作为一直判断的条件 也可以选择单调递减为一致判断的条件
#这两种判断条件的区别在于边界该如何修改
#实际上本题的 重点 也在于边界该如何修改 以及while循环的条件该怎样判断

#解法一
'''
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        idx, ends = 0, len(arr) - 1
        while idx <= ends:     #利用二分查找，根据题目的单调性来作答，不断判断中心值和周围值的大小关系
            mid = idx + (ends - idx)//2
            if arr[mid] < arr[mid + 1]:
                idx = mid + 1    #总是指向下一个可能为峰值的索引，故直接返回idx
            else:
                ends -= 1    #不满足条件证明该区域不是单调递增区域 因此逐步收缩范围
        return idx
'''

#解法二
'''
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        idx, ends = 0, len(arr) - 1
        while idx <= ends:
            mid = idx + (ends - idx)//2
            if arr[mid - 1] < arr[mid]:
                idx = mid + 1     #这里idx 每次都是mid + 1也就意味着如果当前mid是峰值，那么idx可能在峰值右边的一位
            else:
                ends -= 1
        return idx - 1
'''

#解法三
'''
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        idx, ends = 0, len(arr)
        while idx + 1 < ends:
            mid = idx + (ends - idx)//2
            if arr[mid - 1] < arr[mid]:
                idx = mid 
            else:
                ends -= 1
        return idx
'''