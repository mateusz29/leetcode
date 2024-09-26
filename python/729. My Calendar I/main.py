class MyCalendar:
    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        for in_start, in_end in self.intervals:
            if start < in_end and end > in_start:
                return False
            
        self.intervals.append([start, end])
        return True
    
# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
print(obj.book(10, 20))
print(obj.book(15, 25))
print(obj.book(20, 30))
