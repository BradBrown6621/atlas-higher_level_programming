-- 16. Say my name
-- Brad Brown
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
