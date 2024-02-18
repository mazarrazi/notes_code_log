# 1. Retrieve a list with data about all 
# female employees who were hired in the 
# year 2000 or after.
# (If you solve the task correctly, SQL
# should return 7 rows)


SELECT 
    hire_date, gender
FROM
    employees
WHERE
    (gender = 'F') AND (hire_date >= '2000-01-01')  ;


# 2. Extract a list with all employees’ 
# salaries higher than $150,000 per annum.


SELECT 
    *
FROM
    salaries
WHERE
     salary > 150000 ;


