import pandas as pd
import os

def create_sample_dataset():
    """
    Crear una muestra pequeña para GitHub
    """
    # Crear directorios si no existen
    os.makedirs('data/sample', exist_ok=True)
    
    try:
        # Leer el archivo original 
        df = pd.read_parquet('/home/.../nyc-taxi-spark-analysis/data/raw/yellow_tripdata_2023-01.parquet')
        
        print(f"Archivo original tiene {len(df)} registros")
        
        # Tomar una muestra pequeña (ej: 1000 registros)
        sample = df.sample(n=1000, random_state=42)
        
        print("Guardando archivos de muestra...")
        
        # Guardar la muestra
        sample.to_parquet('data/sample/taxi_sample.parquet')
        sample.to_csv('data/sample/taxi_sample.csv', index=False)
        
        print(f"Muestra guardada con {len(sample)} registros")
        print(f"Archivos guardados en: data/sample/")
        
        # Mostrar información básica de la muestra
        print("\nInformación de la muestra:")
        print(sample.info())
        
    except FileNotFoundError:
        print("Error: No se encuentra el archivo original. Asegúrate de haber descargado los datos primero.")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    create_sample_dataset()