# 1. Select all employees whose average salary is higher than $120,000 per annum.

SELECT

    *, AVG(salary)

FROM

    salaries

WHERE

    salary > 120000

GROUP BY emp_no

ORDER BY emp_no;

# or

SELECT

    *, AVG(salary)

FROM

    salaries

GROUP BY emp_no

HAVING AVG(salary) > 120000;
