# 1. Extract all individuals from the ‘employees’ table whose first name contains “Jack”.

```MySQL
SELECT 
    *
FROM
    employees
WHERE
    first_name LIKE ('%jack%');
```


# 2. Once you have done that, extract another list containing the names of employees that do not contain “Jack”.

```MySQL
SELECT 
    *
FROM
    employees
WHERE
    first_name NOT LIKE ('%jack%');
```


