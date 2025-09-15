CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
        SELECT DISTINCT salary
        FROM Employee e1
        WHERE ( SELECT COUNT(DISTINCT salary)
                FROM Employee e2
                WHERE e1.salary <= e2.salary ) = N
  );
END