WITH trajectory_speed_summary AS (
    SELECT
        track_id,
        Min(speed) as min_speed_recorded_for_track,
        Max(speed) as max_speed_recorded_for_track,
        Avg(speed) as avg_speed_recorded_for_track
    FROM
        trajectory_information
    GROUP BY track_id
)

SELECT
    *
FROM
    trajectory_speed_summaryf