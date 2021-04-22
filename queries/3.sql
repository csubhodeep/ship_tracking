/*Show the ranking of the engine types (engine_name) in relation to the maximum speed shown*/


WITH
`engine_speed` AS (
    SELECT
        s.engine1_name,
        MAX(p.SPEED) AS max_speed
    FROM ship_engines s
    LEFT JOIN position_data p
        USING (SHIP_ID)
    GROUP BY s.engine1_name
)

SELECT
    engine1_name,
    RANK() OVER(ORDER BY max_speed DESC) AS rank
FROM `engine_speed`