import pandas as pd

class DataUtils:
    def __init__(self):
        pass

    def df_from_csv(self, vechile_path, trajectory_path):
        

        df_vehicle = pd.read_csv(vechile_path)
        df_trajectory = pd.read_csv(trajectory_path)

        df_vehicle = df_vehicle.head(5)
        df_trajectory = df_trajectory.head(5)
        return df_vehicle, df_trajectory
