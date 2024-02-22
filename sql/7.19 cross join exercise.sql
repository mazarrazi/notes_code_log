# 1. Use a CROSS JOIN to return a list with all possible combinations between managers from the _dept_manager_ table and department number 9.

SELECT
	m.*, d.*
    # m.emp_no, d.dept_no
FROM
	dept_manager m
CROSS JOIN
	departments d
WHERE 
	d.dept_no = 'd009'
ORDER BY 
	emp_no ;
