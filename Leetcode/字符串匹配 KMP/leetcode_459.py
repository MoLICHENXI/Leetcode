#KMP算法查看子集


class Solution:
    def next(self, s):
        #构建前缀表
        next = ['' for i in range(len(s))]
        j = 0  #指向前缀
        i = 1  #指向后缀
        next[0] = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j - 1]
            if s[i] == s[j]:
                j += 1
                next[i] = j
            next[i] = j
        return next

    def repeatedSubstringPattern(self, s: str) -> bool:
        s = list(s)
        next = self.next(s)
        if len(s)%(len(s)-next[-1]) == 0 and next[-1] != 0:   #这里要求next[-1] != 0 是因为'abac'这种情况出现，要求最后一位必须匹配上，且len(s) -next[-1]能被len(s)整除
            return True
        return False

X = Solution()
print(X.repeatedSubstringPattern('abac'))