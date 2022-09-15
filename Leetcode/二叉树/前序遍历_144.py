#二叉树的前序遍历

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

#迭代的思想
class Solution:
    def preorderTraversal(self, root: TreeNode):
        #res用于存储结果
        res = list()
        if not root:
            return res
        #stack用于手动表示递归中的调用栈
        stack = []
        node = root
        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right
        return res


#递归的思想
    def preorderTravelsal(self,root):
        record = []
        def digui(root):
            #结束条件
            if root == None:
                return
            record.append(root.val)
            #递归
            digui(root.left)
            digui(root.right)

        digui(root)
        return record
