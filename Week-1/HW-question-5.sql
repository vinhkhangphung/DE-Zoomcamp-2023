SELECT
    (
        SELECT
            COUNT(*)
        FROM
            green_taxi_data
        WHERE
            DATE(lpep_pickup_datetime) = '2019-01-01'
            AND (passenger_count = 2)
    ) AS passenger_2,
    (
        SELECT
            COUNT(*)
        FROM
            green_taxi_data
        WHERE
            DATE(lpep_pickup_datetime) = '2019-01-01'
            AND (passenger_count = 3)
    ) AS passenger_3