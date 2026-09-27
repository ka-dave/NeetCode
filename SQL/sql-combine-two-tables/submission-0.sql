-- Write your query below
SELECT first_name, last_name, city,
    CASE WHEN person.person_id = address.person_id THEN state
    ELSE 'null'
END AS state 
FROM person
LEFT JOIN address ON person.person_id = address.person_id;