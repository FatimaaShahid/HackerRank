
/*
    Enter your query here and follow these instructions:
    1. Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
    2. The AS keyword causes errors, so follow this convention: "Select t.Field From table1 t" instead of "select t.Field From table1 AS t"
    3. Type your code immediately after comment. Don't leave any blank line.
*/

WITH CityLengths AS (
    SELECT CITY, LENGTH(CITY) AS name_length
    FROM STATION
)
(
    SELECT CITY, name_length
    FROM CityLengths
    ORDER BY name_length ASC, CITY ASC
    FETCH FIRST 1 ROW ONLY
)
UNION ALL
(
    SELECT CITY, name_length
    FROM CityLengths
    ORDER BY name_length DESC, CITY ASC
    FETCH FIRST 1 ROW ONLY
);


