class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = []
        self.size = 0
        self.maxSize = maxSize

    def push(self, x: int) -> None:
        if self.size < self.maxSize:
            self.stack.append(x)
            self.size += 1

    def pop(self) -> int:
        if self.size != 0:
            self.size -= 1
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        amount = k if self.size > k else self.size

        for i in range(amount):
            self.stack[i] += val


# Your CustomStack object will be instantiated and called as such:
obj = CustomStack(3)
obj.push(1)
print(obj.stack)
obj.push(2)
print(obj.stack)
print(obj.pop())
print(obj.stack)
obj.push(2)
print(obj.stack)
obj.push(3)
print(obj.stack)
obj.push(4)
print(obj.stack)
obj.increment(5, 100)
print(obj.stack)
obj.increment(2, 100)
print(obj.stack)
print(obj.pop())
print(obj.stack)
print(obj.pop())
print(obj.stack)
print(obj.pop())
print(obj.stack)
print(obj.pop())
print(obj.stack)
