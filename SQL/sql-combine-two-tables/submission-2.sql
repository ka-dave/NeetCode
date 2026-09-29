-- Write your query below
SELECT person.first_name, person.last_name, address.city,
    CASE WHEN person.person_id = address.person_id THEN state
    ELSE NULL
    END AS state
FROM person
LEFT JOIN address ON person.person_id = address.person_id;