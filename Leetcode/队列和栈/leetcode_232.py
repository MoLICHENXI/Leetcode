#使用两个list完成队列的操作

class MyQueue:
    # 用两个list模拟栈结构
    def __init__(self):
        self.stack_in = []  # 一个用于入栈
        self.stack_out = []  # 一个用于弹出

    # 压入栈即可
    def push(self, x: int) -> None:
        self.stack_in.append(x)

    # 弹出操作 需要先看栈是否为空 再看弹出栈是否为空  如果不为空就直接弹出 否则要把输入栈的数值送入弹出栈
    def pop(self) -> int:
        if self.empty():
            return None

        if self.stack_out:
            return self.stack_out.pop()
        else:  # 把压入栈的所有数据送入弹出栈
            for i in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    # 查看队首值，其实就是可以先弹出，在原样送回去，在这里就是送回弹出栈的队尾
    def peek(self) -> int:
        a = self.pop()
        self.stack_out.append(a)
        return a

    # 判断是否为空
    def empty(self) -> bool:
        return not (self.stack_out or self.stack_in)