class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_val = self.getMin()

        if min_val is None or val < min_val:
            min_val = val
        
        self.stack.append([val, min_val])

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
print(obj.stack)
obj.push(-2)
print(obj.stack)
obj.push(0)
print(obj.stack)
obj.push(-3)
print(obj.stack)
print(obj.getMin())
obj.pop()
print(obj.stack)
print(obj.top())
print(obj.stack)
print(obj.getMin())