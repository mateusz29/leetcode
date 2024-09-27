class MyCalendarTwo:
    def __init__(self):
        self.intervals = []
        self.intervals2 = []

    def book(self, start: int, end: int) -> bool:
        for int2_start, int2_end in self.intervals2:
            if start < int2_end and end > int2_start:
                return False
    
        for int_start, int_end in self.intervals:
            if start < int_end and end > int_start:
                self.intervals2.append([max(start, int_start), min(end, int_end)])
            
        self.intervals.append([start, end])
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
obj = MyCalendarTwo()
print(obj.book(10, 20))
print(obj.book(50, 60))
print(obj.book(10, 40))
print(obj.book(5, 15))
print(obj.book(5, 10))
print(obj.intervals)
print(obj.intervals2)
print(obj.book(25, 55))
print(obj.intervals)
print(obj.intervals2)
