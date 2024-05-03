import sys
import os
from pathlib import Path
import pandas as pd

# Add parent directory to path to import modules from src
rpath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if rpath not in sys.path:
    sys.path.append(rpath)

sys.path.append(str(Path(__file__).parent.parent.parent))
from utils.data_utils import DataUtils

def _extract_data_from_csv():
    vechile_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'vechile_data.csv'))
    trajectory_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data', 'tragjectory_data.csv'))

    data_utils = DataUtils()
    vehicle_df, trajectory_df = data_utils.df_from_csv(vechile_path, trajectory_path)

    return [vehicle_df, trajectory_df]

