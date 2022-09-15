#所有二叉树的路径


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def binaryTreePaths(self, root):
        path = ''
        result = list()
        self.dfs(root, path, result)
        return result

    def dfs(self, root, path, result):
        path += str(root.val)
        # 找到了叶子结点
        if not root.left and not root.right:
            return result.append(path)

        if root.left:
            path += '->'
            self.dfs(root.left, path, result)
            path = path[:-2]
        # if root.left:
        #     self.dfs(root.left, path + '->', result)

        if root.right:
            path += '->'
            self.dfs(root.right, path, result)
            path = path[:-2]
        # if root.right:
        #     self.dfs(root.right, path + '->', result)