# 1. How many annual contracts with a value higher than or equal to $100,000 have been registered in the _salaries_ table?

SELECT 
    COUNT(*)
FROM
    salaries
WHERE
	salary >= 100000;


# 2. How many annual contracts with a value higher than or equal to $100,000 have been registered in the _salaries_ table? Only the number of distinct salaries.

SELECT 
    COUNT(DISTINCT salary)
FROM
    salaries 
WHERE
	salary >= 100000;


# 3. How many managers do we have in the “employees” database? Use the star symbol ``(*)`` in your code to solve this exercise.

SELECT 
    COUNT(*)
FROM
    dept_manager ;

# or

SELECT 
    COUNT(emp_no)
FROM
    dept_manager ;
