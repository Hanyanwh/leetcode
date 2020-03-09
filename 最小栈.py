# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
#
# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。
# 示例:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#


class LNode:
    def __init__(self, initdata, initindex):
        self.data = initdata
        self.index = initindex
        self.next_ = None
    # def setData(self, data)
    #     self.__data = data
    # def setNext(self, next)
    #     self.__next = next
    # def getData(self)
    #     return self.__data
    # def getNext(self)
    #     return self.__next


class MinStack:

    """
    链表排序加栈
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_stack = []
        self.listHead = LNode(0, 0)

    def push(self, x: int) -> None:
        p = self.listHead
        self.min_stack.append(x)
        q = LNode(x, len(self.min_stack))
        while p:
            if not p.next_:
                p.next_ = q
                return
            elif p.next_ and not p.next_.next_:
                if p.next_.data > x:
                    temp = p.next_
                    p.next_ = q
                    q.next_ = temp
                    return
                else:
                    p.next_.next_ = q
                    return
            elif p.next_ and p.next_.next_:
                if p.next_.data > x:
                    temp = p.next_
                    p.next_ = q
                    q.next_ = temp
                    return
                elif p.next_.data <= x and (p.next_.next_.data > x):
                    temp = p.next_.next_
                    p.next_t.next_ = q
                    q.next_ = temp
                    return
                else:
                    p = p.next_

    def pop(self) -> None:
        if not self.min_stack: return None
        index = len(self.min_stack)
        self.min_stack.pop()
        p = self.listHead
        while p.next_:
            if p.next_.index == index:
                temp = p.next_
                p.next_ = p.next_.next_
                del temp
                return

    def top(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return 0

    def getMin(self) -> int:
        if not self.min_stack:
            return 0
        return self.listHead.next_.data

    def getLink(self):
        p = self.listHead
        while p.next_:
            print(p.next_.data)
            p = p.next_


class MinStackEnd:
    """
        辅助栈存储当前栈内最小元素

    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stackMin = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not len(self.stackMin) or x <= self.stackMin[-1]:
           self.stackMin.append(x)

    def pop(self) -> None:
        temp = self.stack.pop()
        if temp == self.stackMin[-1]:
            self.stackMin.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            return 0

    def getMin(self) -> int:
        if not self.stackMin: return 0
        return self.stackMin[-1]


class MinStackEndEnd:
    """
        栈中存数组

    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append([x, x])
        else:
            self.stack.append([x, x if x < self.stack[-1][1] else self.stack[-1][1]])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        else:
            return 0

    def getMin(self) -> int:
        if not self.stack: return 0
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
minStack.getMin()

# print(minStack.top())
# print(minStack.getMin())
# minStack.getLink()




