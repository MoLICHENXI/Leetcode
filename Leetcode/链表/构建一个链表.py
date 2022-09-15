class ListNode:
    def __init__(self,data,next = None):  #默认一个节点的next部分为None
        self.data = data
        self.next = next
    def __str__(self):
        return str(self.data)

class LinkedList:
    def __init__(self,head):       #给链表设置一个头结点  头结点指向第一个节点ListNode
        self.head = head
    def __len__(self):             #求链表的长度
        curr = self.head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next
        return count

#如何创建链表
node1 = ListNode(1)                #给node1一个data值
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2                 #将node1的next指针指向node2
node2.next = node3
x = LinkedList(node1)
print(x.head)
print(len(x))