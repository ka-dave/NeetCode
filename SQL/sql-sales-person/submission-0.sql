-- Write your query below
SELECT sales_person.name FROM sales_person
WHERE sales_id NOT IN (
    SELECT orders.sales_id FROM orders
    JOIN company ON company.com_id = orders.com_id
    WHERE company.name = 'CRIMSON'
);