# Definition for a binary tree node.


#二叉搜索树删除节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 1、没找到
        if not root:
            return root
        # 2、找到了 叶子结点
        if root.val == key:
            # 此时直接删除叶子结点 返回None
            if not root.left and not root.right:
                del root
                return None

            # 3、找到了 只有左子树 直接将左子树接上来
            if not root.right and root.left:
                tmp = root
                root = root.left
                del tmp
                return root

            # 4、找到了 只有右子树 直接将右子树接上来
            if not root.left and root.right:
                tmp = root
                root = root.right
                del tmp
                return root

            # 5、找到了 左右子树都有 那就把左子树放到右子树最左边的叶子结点的左边即可
            if root.left and root.right:
                tmp = root.right
                while tmp.left != None:
                    tmp = tmp.left
                # 接上
                tmp.left = root.left
                tmp = root
                root = root.right
                del tmp
                return root

        #这里是使用了root的left和right指针承载了返回的值
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root