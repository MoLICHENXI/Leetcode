#x的平方根
#本题是模拟sqrt(x)函数的计算方法，这里可以使用二分法
#也可以使用牛顿近似法不断逼近所求零点

#解法一:二分查找
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        idx = 1
        ends = x
        while idx <= ends:
            mid = idx + (ends - idx)//2
            if mid **2 == x:
                return mid
            elif mid **2 > x:
                ends = mid - 1
            elif mid **2 < x:
                idx = mid + 1
        return ends
'''

#解法二：牛顿近似法
#明确问题 我们要求的就是给定一个C，求C的平方根，等价于f(x) = X**2 -C的解；选择初始迭代值X0 = C
'''
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        c, x0 = float(x), float(x)
        while True:
            x1 = (x0 + c/x0)/2
            if abs(x0 - x1) < 10e-6:
                break
            x0 = x1
        return int(x0)
'''

X=Solution()
print(X.mySqrt(25))