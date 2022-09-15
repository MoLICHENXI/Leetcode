#解法一：列表推导 很巧妙！

class Solution:
    def letterCombinations(self, digits: str) -> list:
        KEY = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        if digits == '':
            return []
        ans = ['']
        for num in digits:
            #初始时，必须用''空字符串和字符串相加得到 即'' + 'a' 得到'a'
            ans = [pre+suf for pre in ans for suf in KEY[num]]
        return ans


#解法二：回溯
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        # 先判断长度、结束条件就是长度等于给定的digit

        n = len(digits)
        # 存放最终结果
        result = []
        # 存放中间结果
        path = str()
        # 对应的映射
        dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def backtracking(digits, index):
            # 如果存储的字长和输入的digits长度相等 则返回
            nonlocal path
            # 则结束条件如下
            if len(path) == n:
                result.append(path)
                return

            # 开始for循环部分

            # 先找当前字母
            letters = dic[digits[index]]
            for i in letters:
                # 处理节点
                path += i
                backtracking(digits, index + 1)
                #回溯处理
                path = path[:-1]

X = Solution()
print(X.letterCombinations('23'))