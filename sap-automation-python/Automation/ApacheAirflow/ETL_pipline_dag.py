from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime
import subprocess

def extract_from_sap():
    # Here you execute the Python script that controls SAP GUI for data extraction.
    subprocess.run(["python", "Sap_integration.py"])

def transform_data():
    # This step is to transform the data extracted from SAP.
    subprocess.run(["python", "data_processing.py"])

def update_powerbi():
    # Here you call the script that updates Power BI.
    subprocess.run(["python", "update_powerbi.py"])

# Define the DAG
default_args = {
    'owner': 'nicolas',
    'start_date': datetime(2024, 10, 1),  # Adjust as necessary for the first run
    'retries': 3,
}

with DAG('sap_to_powerbi_pipeline',
         default_args=default_args,
         schedule_interval='0 0 * * 1',  # Runs every Monday at midnight
         catchup=False) as dag:
   
    # DAG tasks       
    start_task = DummyOperator(task_id='start')           
    
    extract_task = PythonOperator(
        task_id='extract_from_sap',
        python_callable=extract_from_sap
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )

    update_powerbi_task = PythonOperator(
        task_id='update_powerbi',
        python_callable=update_powerbi
    )
    
    end_task = DummyOperator(task_id='end')
           
    # Define the order of task execution
    start_task >> extract_task >> transform_task >> update_powerbi_task >> end_task

