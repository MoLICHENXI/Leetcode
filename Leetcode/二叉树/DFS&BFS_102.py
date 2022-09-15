#层序遍历二叉树

'''
#递归解法
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        def digui(root, depth, result):
            if not root:
                return []
            if len(result) == depth:
                #表示开始层序遍历
                result.append([])
            result[depth].append(root.val)
            if root.left:
                digui(root.left, depth + 1, result)
            if root.right:
                digui(root.right, depth + 1, result)
        digui(root, 0, result)
        return result


#迭代解法
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        record = []
        # root为空树，返回为空
        if not root:
            return record
            # 把需要遍历的数字填入队列que中
        # 先把根节点写入队列中
        que = deque([root])
        # 只要que不为空，也就是需要遍历
        while que:
            # 每层需要遍历的个数就是len(que)的长度
            q = len(que)
            # 存储每层的遍历结果
            result = []
            for i in range(q):
                # 从左边出队列
                node = que.popleft()
                result.append(node.val)
                # 如果当前取出的节点有左子树，存入子树的节点
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
            # 每一次循环，result都清零
            record.append(result)
        return record
'''