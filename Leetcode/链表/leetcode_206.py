#反转链表
#递归解法
#还是要明确递归中的回溯条件。


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # base case当链表为空或只有head的时候，反转结果就是自己
        if not head or not head.next:
            return head

        last = self.reverseList(head.next)
        # 经过递归调用之后，可以认为self.reverseList()返回了head节点后面【节点】反转的结果
        # 即1-> 【2 <-3 <-4 <-5】
        # 注意，这里2还指向Null
        # 因此下一步需要让2指向1，即head.next（表示2）.next = head
        # 让head.next的节点指向head
        head.next.next = head
        # 让head节点指向None
        head.next = None
        return last
# X.reverseList()