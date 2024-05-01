from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime, timedelta
import pandas as pd
from sqlalchemy import create_engine
import os,sys

from dags.config import DBConfig


# (adjust for prod/staging/dev)
CSV_FILE_PATH = "...data/data.csv"

TARGET_TABLE = "full_traffic_data"


def read_and_print_csv_head(**kwargs):
    """
    Reads the CSV file, prints the head, and prepares data for loading.
    """
    import pandas as pd

    csv_path = CSV_FILE_PATH

    try:
        df = pd.read_csv(csv_path)
        print(df.head(5)) 

        #

        # kwargs['ti'] is the TaskInstance object, used to access XCom results
        kwargs['ti'].xcom_push(key='data_to_load', value=df.to_dict(orient='records'))

    except Exception as e:
        raise AirflowException(f"Error reading CSV file: {e}")


def load_data_to_postgres(**kwargs):
    """
    Loads the prepared data (from XCom) into the Postgres table.
    """
    import psycopg2

    db_config = DBConfig.load()

    # Build the connection string using config values
    connection_string = f"postgresql+psycopg2://{db_config['DATABASE_USER']}:{db_config['DATABASE_PASSWORD']}@{db_config['DATABASE_HOST']}:{db_config['DATABASE_PORT']}/{db_config['DATABASE_NAME']}"

    conn = psycopg2.connect(connection_string)

    cur = conn.cursor()

    
    # sql = f"""
    # INSERT INTO {TARGET_TABLE} ()
    # VALUES ()
    # """

    try:
        data_to_load = kwargs['ti'].xcom_pull(key='data_to_load')

        for row in data_to_load:
            cur.execute(sql, tuple(row.values()))

        conn.commit()

    except Exception as e:
        conn.rollback()
        raise AirflowException(f"Error loading data to Postgres: {e}")

    finally:
        cur.close()
        conn.close()


with DAG(
    dag_id="csv_to_postgres_dag",
    start_date=datetime(2024, 5, 1),  
    schedule_interval=None,  
    default_args={
        "owner": "airflow",
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
    },
) as dag:

    read_csv_task = PythonOperator(
        task_id="read_and_print_csv",
        python_callable=read_and_print_csv,
        provide_context=True,
    )

    load_data_task = PythonOperator(
        task_id="load_data_to_postgres",
        python_callable=load_data_to_postgres,
        provide_context=True,
    )

    read_csv_task >> load_data_task
