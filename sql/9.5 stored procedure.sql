# 1. Create a procedure that will provide the average salary of all employees. Then call the stored procedure

SELECT
		AVG(salary) AS avg_salary
	FROM
		salaries

USE employees ;

DROP PROCEDURE IF EXISTS avg_sal ; 

DELIMITER $$

CREATE PROCEDURE avg_sal()
BEGIN
	SELECT
		AVG(salary) AS avg_salary
	FROM
		salaries ;
END $$

DELIMITER ;

call avg_sal()
