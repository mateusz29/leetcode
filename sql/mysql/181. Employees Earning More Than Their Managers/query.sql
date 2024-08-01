# Write your MySQL query statement below
SELECT E.name AS Employee
FROM Employee E
JOIN Employee M
ON E.ManagerId = M.Id
WHERE E.Salary > M.Salary