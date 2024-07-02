import pandas as pd
from typing import List

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    return pd.DataFrame(student_data, columns=['student_id', 'age'])

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    return [players.shape[0], players.shape[1]]

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id'] == 101, ['name', 'age']]

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees

df = createDataframe([[1,15],[2,11],[3,11],[4,20]])
print(df)

size = getDataframeSize(df)
print(size)

three_rows = selectFirstRows(df)
print(three_rows)

selected_data = selectData(df)
print(selected_data)