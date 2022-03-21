# Write your MySQL query statement below

SELECT 
    IF(b.cnt >= 1, b.sal, NULL) AS SecondHighestSalary 
FROM (
    SELECT 
     COUNT(*) AS cnt,
     a.sal AS sal
    FROM 
     (SELECT salary AS sal, dense_rank() over (order by salary desc) AS ranking 
      FROM Employee) a
    WHERE a.ranking = 2
    ) b
