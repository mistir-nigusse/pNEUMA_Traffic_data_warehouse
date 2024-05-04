WITH trajectory_speed_summary AS (
    SELECT
        *
    FROM {{ ref('trajectory_speed_summary') }}
    WHERE avg_speed_recorded_for_track > 40
)

SELECT 
    type,
    track_id,
    trajectory_speed_summary.avg_speed_recorded_for_track
FROM
    vehicle_information
Join trajectory_speed_summary
USING(track_id)