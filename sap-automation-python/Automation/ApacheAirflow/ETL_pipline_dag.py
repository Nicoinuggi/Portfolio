  from airflow import DAG
  from airflow.operators.python_operator import PythonOperator
  from datetime import datetime
  import subprocess
  
  def extract_from_sap():
      # Aquí ejecutas el script de Python que controla SAP GUI para la extracción de datos.
      subprocess.run(["python", "Sap_integration.py"])
  
  def transform_data():
      # Este paso sería para transformar los datos extraídos de SAP.
      subprocess.run(["python", "data_processing.py"])
  
  def update_powerbi():
      # Aquí llamas el script que actualiza Power BI.
      subprocess.run(["python", "update_powerbi.py"])
  
  # Definir el DAG
  default_args = {
      'owner': 'nicolas',
      'start_date': datetime(2024, 1, 1),
      'retries': 1,
  }
  
  with DAG('sap_to_powerbi_pipeline',
           default_args=default_args,
           schedule_interval='@daily',  # Cambia esto según tu frecuencia deseada.
           catchup=False) as dag:
  
      # Tareas del DAG
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

    # Definir el orden de ejecución de las tareas
    extract_task >> transform_task >> update_powerbi_task
