# 1. Extract a list containing information about all managers’ employee number, first and last name, department number, and hire date. Use the old type of join syntax to obtain the result.
 
# Old JOIN syntax (using WHERE)
SELECT
	e.emp_no, e.first_name, e.last_name, m.dept_no, e.hire_date
FROM     
	employees e, dept_manager_dup m
WHERE
	e.emp_no = m.emp_no
ORDER By emp_no ;

 
# NEW JOIN syntax (using JOIN)
SELECT
	e.emp_no, e.first_name, e.last_name, m.dept_no, e.hire_date
FROM     
	employees e 
JOIN
	dept_manager_dup m ON e.emp_no = m.emp_no
ORDER By emp_no ;

# both have same output of 22 rows
