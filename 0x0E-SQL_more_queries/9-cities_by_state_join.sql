-- select cities california
SELECT cities.id, cities.name, states.name
FROM hbtn_0d_usa.cities, hbtn_0d_usa.states
WHERE states.id = cities.state_id
ORDER BY cities.id ASC;
