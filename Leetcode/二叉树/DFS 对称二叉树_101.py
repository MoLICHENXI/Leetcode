#对称二叉树

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.duichentreee(root.left, root.right)
        # 1、需要传递的参数和返回值

    def duichentreee(self, left_tree, right_tree):
        # 2、结束条件
        if not left_tree and right_tree:
            return False
        elif left_tree and not right_tree:
            return False
        elif not left_tree and not right_tree:
            return True
        elif left_tree.val != right_tree.val:
            return False

        # 3、单次递归的操作
        outside = self.duichentreee(left_tree.left, right_tree.right)
        inside = self.duichentreee(left_tree.right, right_tree.left)
        return outside & inside
'''