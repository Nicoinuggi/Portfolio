# docker/airflow/Dockerfile
FROM apache/airflow:2.6.3-python3.9

# Instalar dependencias
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar los DAGs al contenedor
COPY ./src/airflow/dags /opt/airflow/dags
