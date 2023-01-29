SELECT
    "Zone"
FROM
    taxi_lookup
WHERE
    "LocationID" = (
        SELECT
            "DOLocationID"
        FROM
            (
                SELECT
                    "DOLocationID",
                    tip_amount
                FROM
                    green_taxi_data
                WHERE
                    "PULocationID" = (
                        SELECT
                            "LocationID"
                        FROM
                            taxi_lookup
                        WHERE
                            "Zone" = 'Astoria'
                    )
                ORDER BY
                    tip_amount DESC
            ) AS t
        LIMIT
            1
    )