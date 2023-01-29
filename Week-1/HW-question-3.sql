SELECT
    COUNT(*)
FROM
    (
        SELECT
            pickTime
        FROM
            (
                SELECT
                    DATE(r.lpep_pickup_datetime) AS pickTime
                FROM
                    green_taxi_data r
            ) AS t
        WHERE
            pickTime = '2019-01-15'
    ) AS t2