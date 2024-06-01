class MinStack:

    def __init__(self):
        self.min_arr = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (not self.min_arr) or (val <= self.min_arr[-1]):
            self.min_arr.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if val == self.min_arr[-1]:
                self.min_arr.pop()
            return val

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return self.stack
        

    def getMin(self) -> int:
        if self.min_arr:
            return self.min_arr[-1]
        return self.min_arr
        


# Your MinStack object will be instantiated and called as such:
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)

assert min_stack.getMin() == -3
assert min_stack.pop() == -3
assert min_stack.top() == 0
assert min_stack.getMin() == -2