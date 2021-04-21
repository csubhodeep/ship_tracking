
/*What was the average number of nautical miles travelled per owner during the noon period 12-14?*/

/*
nautical_miles = ACOS [(sin(Lat_place_1*PI()/180)*sin(Lat_place_2*PI()/180)+

cos(Lat_place_1*PI()/180)*cos(Lat_place_2*PI()/180)*

cos(Lon_place_2*PI()/180-Lon_place_1*PI()/180)) ] *3443.8985
*/

WITH
`position_at_12` AS (
    SELECT
        SHIP_ID,
        LON,
        LAT,
        DATE(TIMESTAMP) AS day
    FROM position_data
    WHERE TIME(TIMESTAMP) BETWEEN '12:00:00' AND '13:00:00'
),

`position_at_14` AS (
    SELECT
        SHIP_ID,
        LON,
        LAT,
        DATE(TIMESTAMP) AS day
    FROM position_data
    WHERE TIME(TIMESTAMP) BETWEEN '13:00:00' AND '14:00:00'
),

`nautical_miles` AS (
    SELECT
        p12.SHIP_ID,
        p12.day,
        (p12.LON-p14.LON)*(p12.LAT-p14.LAT) AS nautical_miles
    FROM `position_at_12` p12
    LEFT JOIN `position_at_14` p14
        USING (SHIP_ID, day)
),

`miles_per_owner_per_day` AS (
    SELECT *
    FROM `nautical_miles` nm
    LEFT JOIN ship_owner so
        USING (SHIP_ID)
)

SELECT
    owner,
    AVG(nautical_miles) AS avg_nautical_miles
FROM `miles_per_owner_per_day`
GROUP BY owner

