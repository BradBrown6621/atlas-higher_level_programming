-- 8. Cities of California
-- Brad Brown
SELECT id, name FROM cities
WHERE state_id = (
	SELECT id FROM states
	WHERE name = 'California'
);
