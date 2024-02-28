# 1.Create a function called ‘emp_info’ that takes for parameters the first and last name of an employee, and returns the salary from the newest contract of that employee.  
# Hint: In the BEGIN-END block of this program, you need to declare and use two variables – v_max_from_date that will be of the DATE type, and v_salary, that will be of the DECIMAL (10,2) type._

  
USE employees ; 

DROP FUNCTION IF EXISTS f_emp_info ;

DELIMITER $$ 

CREATE FUNCTION f_emp_info(p_first_name VARCHAR(255), p_last_name VARCHAR(255)) RETURNS DECIMAL(10,2)
DETERMINISTIC

BEGIN
DECLARE v_max_from_date DATE ;
DECLARE v_salary DECIMAL (10,2) ;

SELECT
	MAX(s.from_date)
INTO
	v_max_from_date
FROM
	employees e
JOIN
	salaries s ON e.emp_no = s.emp_no
WHERE
	p_first_name = e.first_name 
    AND p_last_name = e.last_name ;

SELECT 
	s.salary
INTO
	v_salary
FROM
	employees e
JOIN
	salaries s ON e.emp_no = s.emp_no 
WHERE
	p_first_name = e.first_name 
    AND p_last_name = e.last_name
    AND v_max_from_date = s.from_date;
    
RETURN v_salary ;
END $$ 

DELIMITER ;

SELECT f_emp_info('Aruna', 'Journel')
