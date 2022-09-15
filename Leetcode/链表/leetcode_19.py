#使用递归完成删除倒数第n个节点

'''
#双指针解法 让快指针先走n步，快慢指针在一起走，当快指针走到最后 慢指针就是倒数第n个
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0,head) #虚拟节点
        slow = dummy
        fast = dummy
        for i in range(n):
            fast = fast.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next


#递归解法
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.curr = 0

    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:   #递归的退出条件
            return None
        head.next = self.removeNthFromEnd(head.next,n)
        self.curr += 1   #只有在弹出栈的时候会加一 入栈后续都被挂起进程
        if self.curr == n:
            return head.next #当前的head 返回head.next也就是2->3->4 如果3是目标值 那么2.next = self.remove(3,n) 而remove(3,n)返回的是3.next 也就是4 所以2.next =4 完成删除
        else:
            return head

'''