/*Show the ranking of the engine types (engine_name) in relation to the maximum speed shown*/


SELECT
    s.engine1_name,
    MAX(p.SPEED) AS max_speed
FROM position_data p
LEFT JOIN ship_engines s
    USING (SHIP_ID)
GROUP BY s.engine1_name
ORDER BY max_speed DESC
