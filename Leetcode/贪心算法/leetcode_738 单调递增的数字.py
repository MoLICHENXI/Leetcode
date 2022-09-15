class Solution:
    def monotoneIncreasingDigits(self, n) -> int:
        res  = list(str(n))
        for i in range(len(res) - 1, 0, -1):
            if int(res[i - 1]) > int(res[i]):
                res[i - 1] = str(int(res[i - 1]) - 1)
                res[i:] = '9' * (len(res) - i)
        return int(''.join(res))

X = Solution()
print(X.monotoneIncreasingDigits(n =1234))