# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


#法一
#使用双端队列，将所有需要遍历的节点存入que中，只取每层(record)中最右边的val作为结果
from collections import deque
class Solution:
    def rightSideView(self, root):
        result = []
        if not root:
            return []
        que =deque([root])
        while que:
            q = len(que)
            record = []
            for i in range(q):
                node = que.popleft()
                record.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            result.append(record[q - 1])
        return result


#法二，使用字典不断获得每个深度的最后一个值
    def rightSideView(self, root: TreeNode):
        rightmost_value_at_depth = dict() # 深度为索引，存放节点的值
        max_depth = -1                    #  初始化最大深度

        queue = deque([(root, 0)])
        while queue:   #元组解包
            node, depth = queue.popleft()

            if node is not None:
                # 维护二叉树的最大深度
                max_depth = max(max_depth, depth)

                # 由于每一层最后一个访问到的节点才是我们要的答案，因此不断更新对应深度的信息即可
                rightmost_value_at_depth[depth] = node.val

                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth + 1)]


#法三 使用深度优先遍历

class Solution:
    def level(self, root, depth, res):
        if not root:
            return
        if len(res) < depth:
            res.append(root.val)
        if root.right:
            self.level(root.right, depth + 1, res)
        if root.left:
            self.level(root.left, depth + 1, res)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.level(root, 1, res)
        return res