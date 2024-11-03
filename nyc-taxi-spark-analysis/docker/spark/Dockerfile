# docker/spark/Dockerfile
FROM bitnami/spark:latest

# Copia el script de transformación a la imagen
COPY ./spark/jobs/taxi_transformations.py /opt/spark/jobs/taxi_transformations.py

# Definir el punto de entrada del contenedor
ENTRYPOINT ["/opt/bitnami/scripts/spark/entrypoint.sh"]
CMD ["spark-submit", "/opt/spark/jobs/taxi_transformations.py"]

