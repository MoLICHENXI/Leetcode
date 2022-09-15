# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not inorder:
            return None

        # 先找到父节点
        node_val = preorder[0]
        root = TreeNode(node_val)

        # 再找到中序遍历的该位置并分隔为左右子树
        left_inorder = inorder[:inorder.index(node_val)]
        right_inorder = inorder[inorder.index(node_val) + 1:]

        # 中序遍历的前一半长度
        left_preorder = preorder[1:len(left_inorder) + 1]
        right_preorder = preorder[len(left_inorder) + 1:]

        root.left = self.buildTree(left_preorder, left_inorder)
        root.right = self.buildTree(right_preorder, right_inorder)

        return root