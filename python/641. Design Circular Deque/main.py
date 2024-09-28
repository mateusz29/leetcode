class MyCircularDeque:
    def __init__(self, k: int):
        self.deque = []
        self.size = k

    def insertFront(self, value: int) -> bool:
        if not self.isFull():
            self.deque.insert(0, value)
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if not self.isFull():
            self.deque.append(value)
            return True
        return False

    def deleteFront(self) -> bool:
        if not self.isEmpty():
            self.deque.pop(0)
            return True
        return False

    def deleteLast(self) -> bool:
        if not self.isEmpty():
            self.deque.pop()
            return True
        return False

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.deque[0]
        return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.deque[len(self.deque) - 1]
        return -1

    def isEmpty(self) -> bool:
        return len(self.deque) == 0

    def isFull(self) -> bool:
        return len(self.deque) == self.size


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