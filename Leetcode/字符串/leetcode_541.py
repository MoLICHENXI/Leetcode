class Solution:
        def reverseStr(self, s: str, k: int) -> str:
            # Two pointers. Another is inside the loop.
            p = 0
            while p < len(s):
                p2 = p + k
                # Written in this could be more pythonic.
                s = s[:p] + s[p: p2][::-1] + s[p2:]   #python能够自动处理溢出的情况
                p = p + 2 * k
            return s

X= Solution()
print(X.reverseStr('abcdefg',8))