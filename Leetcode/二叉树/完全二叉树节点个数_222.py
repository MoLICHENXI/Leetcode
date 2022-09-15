#求完全二叉树节点个数



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#迭代法
from collections import deque
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        que = deque([root])
        res = 0
        while que:
            q = len(que)
            for i in range(q):
                node = que.popleft()
                res += 1
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        return res


