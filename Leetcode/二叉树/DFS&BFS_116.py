#leetcode 116


#递归
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def dfs(root):
            if not root:
                return
            #有两个节点
            node1 = root.left
            node2 = root.right
            #只要node1不为空 那它就能一直指向node2，即使node2为空
            while node1:
                node1.next = node2
                node1 = node1.right
                node2 = node2.left
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return root