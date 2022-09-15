#正向递归
#这里面每次的head.next都是指向的两两交换节点的'新尾节点'
#例如 1->2 这个head在节点进行交换后是1，也就是1.next = swap(rest)


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    #正向递归
    '''
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: #为空或者只有一位
            return head
        rest = head.next.next
        newhead = head.next
        newhead.next = head
        head.next = self.swapPairs(rest)
        return head

    '''
    #反向递归
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        next = head.next   #next指向1->2中的2、3->4中的4
        head.next = self.swapPairs(next.next) #head就是1、3这种新的尾节点
        next.next = head
        return next
