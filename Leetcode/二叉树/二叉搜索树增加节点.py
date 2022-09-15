# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    #法一：递归函数有返回值
    #因为二叉搜索树可以将需要加入的节点直接放在叶子结点后，形成新的叶子结点，因此终止条件就是root = None，这个时候需要创建新的TreeNode(val)
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:

        #在树的末端加入
        if not root:
            node = TreeNode(val)
            return node

        #利用二叉树的性质
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)

        return root

    #法二：递归函数没有返回值
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        #也可以选择不返回值

        #如果树是空树
        newnode = TreeNode(val)
        if not root:
            return newnode

        #开始递归
        if not root.left and root.val > val:
            root.left = newnode
        if not root.right and root.val < val:
            root.right = newnode

        if root.val < val:
            self.insertIntoBST(root.right, val)
        elif root.val > val:
            self.insertIntoBST(root.left, val)
        return root

    #法三：迭代法
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 迭代法

        if not root:
            return TreeNode(val)
        # 先创建两个节点
        parent = root
        cur = root
        while cur != None:
            parent = cur
            # 当前节点的迭代
            cur = cur.left if cur.val > val else cur.right
        # 退出条件一定是cur == None，此时parent指向的是叶子结点
        if parent.val < val:
            parent.right = TreeNode(val)
        else:
            parent.left = TreeNode(val)
        return root
