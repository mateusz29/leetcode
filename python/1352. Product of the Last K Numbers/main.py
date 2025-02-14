class ProductOfNumbers:
    def __init__(self):
        self.products = [1]
        self.size = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.products = [1]
            self.size = 0
        else:
            self.products.append(self.products[self.size] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        if self.size < k:
            return 0
        return self.products[self.size] // self.products[self.size - k]


# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
print(obj.getProduct(2))
print(obj.getProduct(3))
print(obj.getProduct(4))
obj.add(8)
print(obj.getProduct(2))
