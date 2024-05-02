
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import psycopg2
from airflow.exceptions import AirflowException

# (adjust for prod/staging/dev)
CSV_FILE_PATH = "...data/data.csv"

def read_and_split_csv(**kwargs):
    """
    Reads the CSV file and splits the data into two tables.
    """
    csv_path = CSV_FILE_PATH

    try:
        df = pd.read_csv(csv_path)

        # Splitting data into two dataframes
        traffic_df = df[['track_id', 'type', 'traveled_d', 'avg_speed']]
        trajectory_df = df[['track_id', 'lat', 'lon', 'speed', 'lon_acc', 'lat_acc', 'time']]

        # Convert NaNs to None
        traffic_df = traffic_df.where(pd.notnull(traffic_df), None)
        trajectory_df = trajectory_df.where(pd.notnull(trajectory_df), None)

        # Pushing the dataframes to XCom
        kwargs['ti'].xcom_push(key='traffic_data', value=traffic_df)
        kwargs['ti'].xcom_push(key='trajectory_data', value=trajectory_df)

    except Exception as e:
        raise AirflowException(f"Error reading CSV file: {e}")

def load_data_to_postgres(table_name, **kwargs):
    """
    Loads the prepared data (from XCom) into the specified Postgres table.
    """
    db_config = {
        'host': 'your_host',
        'database': 'your_database',
        'user': 'your_username',
        'password': 'your_password',
        'port': 'your_port'
    }

    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()

    try:
        data = kwargs['ti'].xcom_pull(key=f'{table_name}_data')

        # Inserting data into the PostgreSQL table
        for _, row in data.iterrows():
            cur.execute(f"INSERT INTO {table_name} VALUES ({', '.join(['%s']*len(row))})", tuple(row))

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
        task_id="read_and_split_csv",
        python_callable=read_and_split_csv,
        provide_context=True,
    )

    load_traffic_data_task = PythonOperator(
        task_id="load_traffic_data_to_postgres",
        python_callable=load_data_to_postgres,
        op_kwargs={'table_name': 'traffic'},
        provide_context=True,
    )

    load_trajectory_data_task = PythonOperator(
        task_id="load_trajectory_data_to_postgres",
        python_callable=load_data_to_postgres,
        op_kwargs={'table_name': 'trajectory'},
        provide_context=True,
    )

    read_csv_task >> [load_traffic_data_task, load_trajectory_data_task]
