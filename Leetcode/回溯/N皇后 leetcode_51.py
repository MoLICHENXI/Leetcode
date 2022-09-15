class Solution:
    def solveNQueens(self, n):
        result = []
        # 先填充一个棋盘
        path = [['.'] * n for i in range(n)]

        # 判断是否满足N皇后的条件
        def isNqueen(path, row, col):
            # 可以不用判断一行是否重复，因为回溯函数的for循环保证了一行只有一个皇后
            # #先判断这个行里有没有皇后
            # for i in range(len(path)):
            #     if path[row][i] == 'Q':
            #         return False

            # 在判断列里有没有皇后
            for i in range(len(path)):
                if path[i][col] == 'Q':
                    return False

            # 判断左上方是否有皇后
            x = row - 1
            y = col - 1
            while x >= 0 and y >= 0:
                if path[x][y] == 'Q':
                    return False
                x -= 1
                y -= 1

            # 因为是按次序回溯，不用判断下方的
            # #判断右下方是否有皇后
            # x = row + 1
            # y = col + 1
            # #注意这里的边界条件
            # while x < len(path) and y < len(path):
            #     if path[x][y] == 'Q':
            #         return False
            #     x += 1
            #     y += 1

            # 判断右上方是否有皇后
            x = row - 1
            y = col + 1
            while x >= 0 and y < len(path):
                if path[x][y] == 'Q':
                    return False
                x -= 1
                y += 1
            # 因为是按次序回溯，不用判断下方的
            # #判断左下方是否有皇后
            # x = row + 1
            # y = col - 1
            # while x < len(path) and y >= 0:
            #     if path[x][y] == 'Q':
            #         return False
            #     x += 1
            #     y -= 1
            # 都满足条件就返回True
            return True

        # 回溯函数
        def backtracking(row):
            # 结束条件
            if row == n:
                res = []
                # path = [['.','.','.','.'],['Q','.','.','.']，[...]]所以对path里面的每一个项都用join函数连接并append到res里
                for i in path:
                    res.append(''.join(i))
                result.append(res[:])
                return

            # 开始处理节点
            # 从第1行开始遍历
            for i in range(len(path)):
                # 当前row的第i个位置 可以填写皇后
                if not isNqueen(path, row, i):
                    continue
                path[row][i] = 'Q'
                backtracking(row + 1)
                path[row][i] = '.'

        backtracking(0)
        return result


#利用三个集合 column diagonal1 diagonal2 判断是否在一列 斜上方 后上方，把放置的列 送入对应的queen的数组中
class Solution:
    def solveNQueens(self, n):
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row: int):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)

        solutions = list()
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        row = ["."] * n
        backtrack(0)
        return solutions

X = Solution()
print(X.solveNQueens(4))
