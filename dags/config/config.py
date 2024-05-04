# config.py

import os,sys
from pathlib import Path


# Define directory paths directly
dag_dir = os.path.join(os.getcwd(), 'dags', 'production')  # Location of production DAGs
dbt_models_dir = os.path.join(os.getcwd(), 'dbt', 'models')  # Location of dbt models
dir = os.path.join(os.getcwd(), 'dbt')
  # Directory for traffic analysis
print(dir)
