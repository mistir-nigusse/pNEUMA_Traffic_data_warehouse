WITH types_summary AS (
    SELECT
        type,
        COUNT(track_id) AS count,
        AVG(traveled_d) AS avg_distance,
        AVG(avg_speed) AS avg_speed
    FROM vehicle_information
    GROUP BY type
)

SELECT * FROM types_summary