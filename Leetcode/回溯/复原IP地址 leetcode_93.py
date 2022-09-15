# class Solution(object):
#     def restoreIpAddresses(self, s):
#         """
#         :type s: str
#         :rtype: List[str]
#         """
#         self.res = []
#
#         def backtrack(s, tmp):
#             if len(s) == 0 and len(tmp) == 4:
#                 self.res.append('.'.join(tmp))
#                 return
#             if len(tmp) < 4:
#                 #因为IP地址一段最长就是3位
#                 for i in range(min(3, len(s))):
#                     p, n = s[:i + 1], s[i + 1:]
#                     #p是保证了len(s) = 0的时候不会记录空数
#                     #int(p)就保证了这些数一定是三位以内
#                     #str(int(p))保证了首位不为0的多位数
#                     if p and 0 <= int(p) <= 255 and str(int(p)) == p:
#                         backtrack(n, tmp + [p])
#
#         backtrack(s, [])
#         return self.res
#
# X = Solution()
# print(X.restoreIpAddresses('101023'))


#清晰做法
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []
        result = []

        def isIP(s, start, end):
            # 传入start = 2, end = 2，实际上是看s[2]这一位
            # 传入start = 2，end = 3，实际上是看s[2:4]这两位
            if start > end:
                return False
            # 如果以0开头且不为1位，则为错误的
            if s[start] == '0' and start != end:
                return False

            # 如果当前的数字不在0 - 255之间 也是错误的 左闭右闭区间 从start 到end这整个区间
            if not 0 <= int(s[start:end + 1]) <= 255:
                return False
            return True

        def backtracking(s, startindex, pointnums):
            # 1、标志的问题 如何结束  只要有三个'.'号就看最后一部分是否满足要求
            if pointnums == 3:
                if isIP(s, startindex, len(s) - 1):
                    result.append(s[:])
                # 看最后一部分是否满足要求
                return

            # 2、怎么切割
            # 3、IP地址的合法性 尤其是0的问题，如果有0，则只能为1维，或者将0接在后面
            # 同时每个点之间的IP地址必须在0 - 255之间
            # 4、for循环的条件
            # 5、回溯需要注意的地方 尤其是'.'
            for i in range(startindex, len(s)):
                # 先切割，并判断是否满足IP地址的要求
                # 只有满足IP格式的才继续进行，否则直接i++
                if isIP(s, startindex, i):
                    # 如果满足 那就把'.'号加在后面 返回新的s
                    # 这里要注意，因为isIP检查的实际上是[startindex: end + 1]之间的值
                    s = s[:i + 1] + '.' + s[i + 1:]
                    pointnums += 1
                    backtracking(s, i + 2, pointnums)
                    # 回溯
                    pointnums -= 1
                    s = s[:i + 1] + s[i + 2:]

        backtracking(s, 0, 0)
        return result