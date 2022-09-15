class Solution:
    def partition(self, s: str):
        if not s:
            return []

        result = []
        path = []

        def backtarcking(s, startindex):
            # 1、结束条件
            # 如果当前要截取的位置超过了整个字符串的长度，就返回
            if startindex >= len(s):
                result.append(path[:])
                return

            # 处理节点
            # 2、for循环里写什么
            # 3、怎么判断回文
            # 4、怎么截取
            for i in range(startindex, len(s)):
                # 先截取字符串
                letter = s[startindex:i + 1]
                # 判断回文，不是回文就继续操作，让i取到下一位
                if letter[::-1] != letter:
                    continue
                # 是回文就添加
                path.append(letter)
                # 递归，从下一位开始
                backtarcking(s, i + 1)
                # 回溯，删掉得到的上一位路径
                path.pop()

        backtarcking(s, 0)
        return result

X = Solution()
print(X.partition('abcba'))