import os

# Define a default directory path (assuming dbt models are in the same directory)
DEFAULT_DIR = os.path.join(os.getcwd(), '..', 'dbt')

def _perform_dbt_transformation():
  # Try to get the directory path from environment variable
  dir = os.getenv('DBT_MODELS_DIR', DEFAULT_DIR)
  return f'cd {dir} && dbt run'

