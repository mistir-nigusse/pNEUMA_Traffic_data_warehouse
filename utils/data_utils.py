import pandas as pd

class DataUtils:
    def __init__(self):
        pass

    def df_from_csv(self, file_path):
        delimiter = ';'

        with open(file_path, 'r') as file:
            lines = file.readlines()
            vehicle_information = []
            trajectory_information = []
            lines = lines[1:]
            for line in lines:
                line = line.strip('\n').strip(' ')
                contents = line.split(delimiter)
                contents = [contents[i].strip() for i in range(len(contents))]

                vehicle_information.append(contents[:4])

                k = 4 # skipping the first 4 columns which are track_id, type, traveled_d, avg_speed
                for i in range(k, len(contents),6):
                    # concatenating the track_id with the trajectory information
                    trajectory_information.append([contents[0],*contents[i:i+6]])

        df_vehicle = pd.DataFrame(data= vehicle_information,columns=['track_id','type','traveled_d','avg_speed'])
        df_trajectory = pd.DataFrame(data= trajectory_information ,columns=['track_id','lat','lon','speed','lon_acc','lat_acc','time'])

        # dropping any rows with NaN values
        df_trajectory.dropna(subset=['lat','lon','speed','lon_acc','time'],inplace=True)
        
        return df_vehicle, df_trajectory
