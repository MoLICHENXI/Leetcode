#构建二叉树


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        zuidazhi = max(nums)
        idx = nums.index(zuidazhi)

        node = TreeNode(zuidazhi)

        left = nums[:idx]
        right = nums[idx + 1:]

        node.left = self.constructMaximumBinaryTree(left)
        node.right = self.constructMaximumBinaryTree(right)
        return node