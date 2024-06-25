import datetime

class Solution:
    def reformatDate(self, date: str) -> str:
        dateSplit = date.split(' ')
        returnDate = dateSplit[2] +  '-' + str(datetime.datetime.strptime(dateSplit[1], '%b').month).zfill(2) + '-' + dateSplit[0][:-2].zfill(2)
        return returnDate

if __name__ == "__main__":
    solution = Solution()
    print(solution.reformatDate("20th Oct 2052"))