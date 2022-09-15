class Solution:
    def evalRPN(self, tokens):
        record = []
        for item in tokens:
            if item not in {'+','-','*','/'}:
                record.append(item)
            else:
                x = record.pop()
                y = record.pop()
                record.append(int(eval(f'{y}{item}{x}')))
        return int(record.pop())


X =Solution()
print(X.evalRPN(["2","1","+","3","*"]))