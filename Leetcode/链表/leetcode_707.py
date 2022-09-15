#这道题涉及了链表的所有操作
#包括从0开始构建节点类Node
#以及一个链表MyLinkedList，初始化链表的两个属性，虚拟节点dummy以及长度len。


class Node:             #节点类
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class MyLinkedList:          #链表的顺序 0-index
    def __init__(self):
        self.dummy = Node() #创建一个虚拟头结点
        self.len = 0        #链表的初始长度为0

    def get(self, index: int) -> int:        #获取第index
        if index < 0 or index >= self.len:
            return - 1
        else:
            curr = self.dummy #指向虚拟节点
            for i in range(index + 1):
                curr = curr.next
            return curr.val

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.dummy.next)        #创建一个节点，值域为val，next域为虚拟头结点的next域指向的原本的头结点
        self.dummy.next = node                        #虚拟头结点的next域指向新添加的节点
        self.len += 1                            #这一步一定要记住，链表长度加一
        return

    def addAtTail(self, val: int) -> None:
        curr = self.dummy                 #指向头结点
        for i in range(self.len):         #找到最后一个节点
            curr = curr.next
        curr.next = Node(val = val, next = None)         #最后一个节点的Next指向新节点
        self.len += 1
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            self.addAtHead(val = val)
            return
        elif index >self.len:
            return
        else:
            curr = self.dummy
            for i in range(index):
                curr = curr.next   #经过index次循环 cur指向的是插入位置之前的一个节点
            node = Node(val = val, next = curr.next)
            curr.next = node
            self.len += 1
            return

    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self.len:
            prev = self.dummy
            curr = self.dummy.next
            for i in range(index):
                prev = curr
                curr = curr.next
            prev.next = curr.next #当前curr指向的节点是要删除的节点
            self.len -= 1
            return
        else:
            return

List = MyLinkedList()
List.addAtHead(1)
print(List)