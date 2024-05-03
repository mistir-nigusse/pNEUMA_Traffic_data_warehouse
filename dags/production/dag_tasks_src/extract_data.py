import sys
from pathlib import Path
import os, sys
# Add parent directory to path to import modules from src
rpath = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
if rpath not in sys.path:
    sys.path.append(rpath)

# sys.path.append(str(Path(__file__).parent.parent.parent))
from src.utils import DataUtils

def _extract_data_from_csv():
    data_utils = DataUtils()
    vehicle_df, trajectory_df = data_utils.df_from_csv('/Users/missy/Desktop/python/Traffic_data_week_2' + "/data/data.csv")
    return [vehicle_df, trajectory_df]
