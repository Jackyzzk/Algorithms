class MinStack(object):
    """
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
链接：https://leetcode-cn.com/problems/min-stack
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.que = []
        self.aux = [float('inf')]

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.que = [x] + self.que
        if x <= self.aux[-1]:
            self.aux.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.que.pop(0) == self.aux[-1]:
            self.aux.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.que[0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.aux[-1]


def main():
    obj = MinStack()
    obj.push(0)
    obj.push(1)
    obj.push(0)
    print(obj.getMin())
    obj.pop()
    print(obj.getMin())


if __name__ == '__main__':
    main()
