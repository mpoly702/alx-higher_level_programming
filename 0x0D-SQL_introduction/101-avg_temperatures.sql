-- Script that displays the average temperature (Fahrenheit)
-- By city ordered by temperature (descending)
SELECT city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;