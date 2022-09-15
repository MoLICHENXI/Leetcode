
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #迭代遍历
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        # 创建一个虚拟头结点
        dummy = ListNode(0 ,head)
        prev = dummy
        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                x = curr.val
                while curr and curr.val == x:
                    curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
        return dummy.next

#递归
def deleteDuplicates(self, head):
    if not head or not head.next:
        return head

    if head.val != head.next.val:
        head.next = self.deleteDuplicates(head.next)
    else:
        move = head.next
        while move and head.val == move.val:
            move = move.next
        return self.deleteDuplicates(move)
    return head


