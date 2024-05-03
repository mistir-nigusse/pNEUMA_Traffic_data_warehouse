import os,sys
from datetime import datetime, timedelta
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

rpath = os.path.abspath('/opt/airflow')  
if rpath not in sys.path:
    sys.path.insert(0, rpath)

from production.extract_data import _extract_data_from_csv
from production.load_data import _load_data_to_db



default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_retry': False,

}


with DAG(
    'ELTDag',
    start_date=datetime(2024,5,3),
    schedule_interval = '@daily',
    catchup = False, 

    ) as dag:

    task1 = PythonOperator(
        task_id='extract_data_from_csv',
        provide_context=True,
        python_callable=_extract_data_from_csv,
        execution_timeout=timedelta(minutes=60),
        
       )

    # Second task is to load data into the database.
    task2 = PythonOperator(
        task_id='load_data',
        provide_context=True,
        python_callable=_load_data_to_db
        )

    task1 >>task2
