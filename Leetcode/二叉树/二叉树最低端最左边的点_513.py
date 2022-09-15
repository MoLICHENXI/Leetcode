#二叉树最低端最左边的点

class TreeNode:
    def __init__(self, val = 0, right = None, left = None):
        self.val = val
        self.left = left
        self.right = right


#层序遍历方法
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root:
            return root
        que = deque([root])
        # while que:
        #     q = len(que)
        #     #先放右边的节点，再放入左边的节点，最后一个放入的节点即为最后一层最左边的节点
        #     for i in range(q):
        #         node = que.popleft()
        #         if node.right:
        #             que.append(node.right)
        #         if node.left:
        #             que.append(node.left)
        #         res = node.val
        # return res

        # 直接取每次层序遍历的第一个节点也可以得到结果
        while que:
            q = len(que)
            res = que[0].val
            for i in range(q):
                node = que.popleft()
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return res


#递归做法
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        maxdepth = float('-inf')
        maxdepth_nums = 0
        def dfs(root, depth):
            #使用nonlocal可以将maxdepth、maxdepth_nums等在函数外声明的变量 变成在dfs函数内可以修改的变量
            nonlocal maxdepth, maxdepth_nums
            if not root.left and not root.right:
                if depth > maxdepth:
                    maxdepth = depth
                    maxdepth_nums = root.val
                return
            if root.left:
                dfs(root.left, depth + 1)
            if root.right:
                dfs(root.right, depth + 1)
            return
        dfs(root, 0)
        return maxdepth_nums