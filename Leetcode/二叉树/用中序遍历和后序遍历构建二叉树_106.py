# Definition for a binary tree node.



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None

        #后序遍历最后一个节点就是父节点
        node_val = postorder[-1]
        root = TreeNode(node_val)

        #先切割中序遍历的数组
        left_inorder = inorder[:inorder.index(node_val)]
        right_inorder = inorder[inorder.index(node_val) + 1:]

        #再切割后序遍历
        left_postorder = postorder[:len(left_inorder)]
        #不要最后一个数字
        right_postorder = postorder[len(left_inorder): len(postorder) - 1]

        #递归
        root.left = self.buildTree(left_inorder,left_postorder)
        root.right = self.buildTree(right_inorder,right_postorder)

        return root