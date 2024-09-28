class MyCircularDeque:
    def __init__(self, k: int):
        self.deque = [0] * k
        self.front = 0
        self.last = k - 1
        self.size = 0
        self.range = k

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.front = (self.front - 1 + self.range) % self.range
            self.deque[self.front] = value
            self.size += 1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.last = (self.last + 1) % self.range
            self.deque[self.last] = value
            self.size += 1
            return True
        return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.front = (self.front + 1) % self.range
            self.size -= 1
            return True
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.last = (self.last - 1 + self.range) % self.range
            self.size -= 1
            return True
        return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.deque[self.front]
        return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.deque[self.last]
        return -1

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.range


# Your MyCircularDeque object will be instantiated and called as such:
obj = MyCircularDeque(3)
print(obj.insertLast(1))
print(obj.insertLast(2))
print(obj.insertFront(3))
print(obj.insertFront(4))
print(obj.getRear())
print(obj.isFull())
print(obj.deleteLast())
print(obj.insertFront(4))
print(obj.getFront())