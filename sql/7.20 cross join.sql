# 1. Return a list with the first 10 employees with all the departments they can be assigned to.

# Hint: Don’t use LIMIT; use a WHERE clause.

SELECT
	e.*, d.*
FROM 
	employees e
CROSS JOIN
	departments d
WHERE
	e.emp_no < 10011
ORDER BY e.emp_no, d.dept_no ;
