import pandas as pd
import os
import argparse
from sqlalchemy import create_engine


def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db_name = params.db_name
    table_name_taxi = params.table_name_taxi
    table_name_lookup = params.table_name_lookup
    url_taxi = params.url_taxi
    url_lookup = params.url_lookup
    csv_name_taxi = 'green_tripdata_2019-01.csv.gz'
    csv_name_lookup = 'taxi+_zone_lookup.csv'

    # download csv
    os.system(f"wget {url_taxi} -O {csv_name_taxi}")
    os.system(f"wget {url_lookup} -O {csv_name_lookup}")

    df = pd.read_csv(csv_name_taxi, compression='gzip')
    df2 = pd.read_csv(csv_name_lookup)

    df.lpep_pickup_datetime = pd.to_datetime(df.lpep_pickup_datetime)
    df.lpep_dropoff_datetime = pd.to_datetime(df.lpep_dropoff_datetime)

    engine = create_engine(
        f'postgresql://{user}:{password}@{host}:{port}/{db_name}')
    # engine.connect()

    df.to_sql(name=f'{table_name_taxi}', con=engine, if_exists='replace')
    df2.to_sql(name=f'{table_name_lookup}', con=engine, if_exists='replace')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Ingest CSV data to Postgres")
    parser.add_argument('--user', help='Username for Postgres')
    parser.add_argument('--password', help='Password for Postgres')
    parser.add_argument('--host', help='Host for Postgres')
    parser.add_argument('--port', help='Port for Postgres')
    parser.add_argument('--db_name', help='Database-name for Postgres')
    parser.add_argument('--table_name_taxi', help='Name of the taxi table')
    parser.add_argument('--table_name_lookup', help='Name of lookup table')
    parser.add_argument('--url_taxi', help='url of taxi data csv')
    parser.add_argument('--url_lookup', help='url of lookup csv')

    args = parser.parse_args()
    main(args)
