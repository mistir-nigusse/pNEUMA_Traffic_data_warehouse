import os
import sys
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine, Integer, String, Float

# Add parent directory to path to import modules from src
rpath = os.getcwd()
if rpath not in sys.path:
    sys.path.append(rpath)

from .data_utils import DataUtils

load_dotenv()

DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

class DBConfig:
    
    @classmethod
    def load(cls):
        return cls()

    def __init__(self):
        self.engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    def insert_vehicle_information_df_to_db(self, vehicle_information_df, table_name):
        vehicle_information_df.to_sql(
            table_name,
            self.engine,
            if_exists='replace',
            index=False,
            chunksize=10000,
            dtype={
                "track_id": Integer,
                "type": String,
                "traveled_d": Float,
                "avg_speed":  Float
            }
        )

    def insert_trajectory_df_to_db(self, trajectory_df, table_name):
        trajectory_df.to_sql(
            table_name,
            self.engine,
            if_exists='replace',
            index=False,
            chunksize=10000,
            dtype={
                "track_id": Integer,
                "lat": Float,
                "lon": Float,
                "speed":  Float,
                "lon_acc":  Float,
                "lat_acc":  Float,
                "time":  Float
            }
        )
        
    def read_data_from_db(self, table_name):
        return pd.read_sql(f"SELECT * FROM {table_name}", self.engine)

def data_to_db(data_file):
    data_reader = DataUtils()
    db = DBConfig()

    vehicle_df, trajectory_df = data_reader.df_from_csv(data_file)

    db.insert_vehicle_information_df_to_db(vehicle_df, 'vehicle_information')
    db.insert_trajectory_df_to_db(trajectory_df, 'trajectory_information')

if __name__ == "__main__":
    data_file = '/Users/missy/Desktop/python/Traffic_data_week_2' + "/data/data.csv" 

    data_to_db(data_file)

    print('Data inserted to db successfully')


