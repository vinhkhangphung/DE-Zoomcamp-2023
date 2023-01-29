SELECT
    trip_distance,
    lpep_pickup_datetime,
    lpep_dropoff_datetime
FROM
    green_taxi_data
WHERE
    trip_distance = (
        SELECT
            MAX(trip_distance)
        FROM
            green_taxi_data
    )