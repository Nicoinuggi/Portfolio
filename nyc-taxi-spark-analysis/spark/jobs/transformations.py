# spark/jobs/taxi_transformations.py
from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.appName("TaxiDataETL").getOrCreate()
    
    # Cargar datos de ejemplo (puedes ajustar el path según tu estructura)
    df = spark.read.csv("/data/raw/taxi_data.csv", header=True, inferSchema=True)
    
    # Transformación simple
    df_filtered = df.filter(df['fare_amount'] > 0)
    
    # Guardar los datos procesados
    df_filtered.write.mode("overwrite").parquet("/data/processed/taxi_data_processed")
    
    spark.stop()

if __name__ == "__main__":
    main()
