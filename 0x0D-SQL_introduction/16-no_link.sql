-- Script that lists all records of the table
-- Second_table of the database hbtn_0c_0
-- Don’t list rows without a name value
-- Results should display the score and the name (in this order)
SELECT score, name FROM second_table
WHERE name IS NOT NULL ORDER BY score DESC;
