
/*What is the average speed per vessel per day across all vessels?*/

WITH
`speed_with_day` AS (
    SELECT
        SHIP_ID,
        DATE(TIMESTAMP) AS day,
        SPEED
    FROM position_data
)

SELECT
    SHIP_ID,
    day,
    AVG(SPEED) AS avg_speed
FROM `speed_with_day`
GROUP BY
    SHIP_ID,
    day
