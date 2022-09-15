

# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):

        # 定义一个虚拟头结点
        dummy = ListNode(0)

        # 一个指向新链表的指针
        start = dummy

        # 进位标志
        jinwei = 0

        # 只有两者都为空才退出循环
        while l1 or l2:
            # 有值就幅值，无值就给0
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum1 = x + y + jinwei
            jinwei = int(sum1 / 10)  # 求进位数

            # 求余数
            start.next = ListNode(sum1 % 10)
            start = start.next
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        # 如果最后都为0 但有个进位项
        if jinwei > 0:
            start.next = ListNode(1)
        return dummy.next