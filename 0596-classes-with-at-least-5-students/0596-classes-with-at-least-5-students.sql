SELECT class
FROM Courses c
GROUP BY class
HAVING count(student) > 4
ORDER BY count(student) DESC