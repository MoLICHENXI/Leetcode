class Solution:
    # 明确反转需要怎么做
    # 1去除多余空格，返回一个list形式
    def removespace(self, s):
        record = []
        left, right = 0, len(s) - 1
        # 去除首位的空格
        while left <= right and s[left] == ' ':
            left += 1
        while left <= right and s[right] == ' ':
            right -= 1
        while left <= right:
            if s[left] != ' ':
                record.append(s[left])
            elif record[-1] != ' ':
                record.append(s[left])
            left += 1
        return record

    # 2反转整个字符串 ,在自己写的时候才知道需要在函数的参数里指定left和right
    def reverseList(self, s, left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return None  # 对list操作 list是可变类型 不用返回

    # 3反转每个子串的顺序
    def reverseSubList(self, s):
        # 注意中间有一个空格
        start, end = 0, 0
        n = len(s)
        while start < n:
            while end < n and s[end] != ' ':
                end += 1
            # 记录了空格出现的位置，end指向空格
            self.reverseList(s, start, end - 1)
            start = end + 1
            end += 1
        return None

    def reverseWords(self, s: str) -> str:
        lst = self.removespace(s)
        self.reverseList(lst, 0, len(lst) - 1)
        self.reverseSubList(lst)
        return ''.join(lst)
