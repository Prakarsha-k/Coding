# Write your MySQL query statement below
SELECT 
    (SELECT unique_id 
     FROM EmployeeUNI 
     WHERE EmployeeUNI.id = Employees.id) AS unique_id, 
    name
FROM 
    Employees;
