#验证二叉搜索树

'''
#法一：使用中序遍历，并生成数组，判断是否为升序

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res = []
        def bfs(root):
            nonlocal res
            que = []
            cur = root
            while que or cur:
                if cur:
                    que.append(cur)
                    cur = cur.left
                else:
                    #取最后一个
                    cur = que.pop()
                    res.append(cur.val)
                    cur = cur.right
            return res
        def sorted(res):
            for i in range(0, len(res) -1):
                if res[i] >= res[i + 1]:
                    return False
            return True
        bfs(root)
        return sorted(res)
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 规律: BST的中序遍历节点数值是从小到大.
        cur_max = -float("INF")

        def __isValidBST(root: TreeNode) -> bool:
            nonlocal cur_max

            if not root:
                return True
            #先找左边的节点，比较完左边的节点，返回True或者False
            is_left_valid = __isValidBST(root.left)
            #比较当前值与前一段内最小值 这里是中序遍历
            if cur_max < root.val:
                cur_max = root.val
            else:
                return False
            #
            is_right_valid = __isValidBST(root.right)

            return is_left_valid and is_right_valid

        return __isValidBST(root)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)

root.left.left = TreeNode(1)
root.left.right = TreeNode(4)

root.right.left = TreeNode(7)
root.right.right = TreeNode(9)

X = Solution()
print(X.isValidBST(root))

