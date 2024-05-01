from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 30),
    'retries': 1,
}

def load_csv_file_prod(**kwargs):
    csv_file_path = '...data/data.csv'
    
    df = pd.read_csv(csv_file_path)
 
    print(df.head(5))

# Create the DAG
dag = DAG(
    'load_csv_file_prod_dag',
    default_args=default_args,
    description='A DAG to load a CSV file in the production environment',
    schedule_interval=None,  # Set to None to disable automatic scheduling
)

load_csv_task = PythonOperator(
    task_id='load_csv_file_task',
    python_callable=load_csv_file_prod,
    provide_context=True,  # Set to True to pass context variables to the Python function
    dag=dag,
)

