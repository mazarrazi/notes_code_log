# Extract all records from the ‘employees’ table, aside from those with employees named John, Mark, or Jacob.

SELECT 
    *
FROM
    employees
WHERE
	first_name NOT IN ('John', 'Mark','Jacob');
