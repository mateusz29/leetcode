import datetime

class Solution:
    def dayOfYear(self, date: str) -> int:
        current_date = datetime.date(int(date[:4]) , int(date[5:7]), int(date[8:]))
        start_of_year = datetime.date(int(date[:4]), 1, 1)
        delta = current_date - start_of_year
        return delta.days + 1

if __name__ == '__main__':
    s = Solution()
    print(s.dayOfYear("2019-01-09"))