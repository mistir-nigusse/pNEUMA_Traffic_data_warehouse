import os, sys
from pathlib import Path

# Add parent directory to path to import modules from src
rpath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src'))
if rpath not in sys.path:
    sys.path.append(rpath)

from utils.db_util import DBConfig

def _load_data_to_db(ti):
    vehicle_df,trajectory_df =  ti.xcom_pull(task_ids='extract_data_from_csv')

    db = DBConfig()
    db.insert_vehicle_information_df_to_db(vehicle_df,'vehicle_information')
    db.insert_trajectory_df_to_db(trajectory_df,'trajectory_information')

