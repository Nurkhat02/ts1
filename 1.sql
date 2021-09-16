CREATE TABLE employee(
    id INT,
    person_name VARCHAR(255),
    street VARCHAR(255),
    sity VARCHAR(255)
);
CREATE TABLE works(
    employee_id INT,
    company_id INT,
    person_name VARCHAR(255),
    company_name VARCHAR(255),
    salary INT
);
CREATE company(
    id INT,
    company_name VARCHAR(255),
    city
);
SELECT employee.id,employee.person_name FROM works INNER JOIN employee ON works.employee_id=employee.id 
WHERE(works.company_name='BigBank');
SELECT employee.id,employee.person_name,employee.sity FROM works INNER JOIN employee ON works.employee_id=employee.id 
WHERE(works.company_name='BigBank');
SELECT employee.id,employee.person_name,employee.street,employee.sity FROM works INNER JOIN employee ON works.employee_id=employee.id 
WHERE(works.company_name='BigBank' AND works.salary>10000);
SELECT employee.id,employee.person_name FROM works INNER JOIN employee ON works.employee_id=employee.id INNER JOIN company ON
works.company_id=company.id 
SELECT employee.id,employee.person_name FROM works INNER JOIN employee ON works.employee_id=employee.id 
WHERE(works.company_name<>'BigBank')
SELECT employee.id, employee.person_name FROM works INNER JOIN employee ON works.employee_id=employee.id
WHERE(works.salary IS NOT NULL works.salary>0)

