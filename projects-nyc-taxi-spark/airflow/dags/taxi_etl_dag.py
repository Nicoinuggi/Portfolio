# airflow/dags/taxi_etl_dag.py
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

default_args = {
    'owner': 'nicolas',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG(
    'taxi_data_etl',
    default_args=default_args,
    description='ETL process for taxi data with Spark',
    schedule_interval='@daily',
    catchup=False,
) as dag:
    
    run_spark_job = BashOperator(
        task_id='run_spark_job',
        bash_command='spark-submit /opt/spark/jobs/taxi_transformations.py'
    )
    
    run_spark_job
