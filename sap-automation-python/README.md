# Automating SAP Data Pipelines with Python and Power BI

## Descripción
Este proyecto automatiza la extracción de datos desde SAP, procesa los datos con pandas, los visualiza en Power BI y automatiza todo el flujo de trabajo utilizando un batch file o Apache Airflow.

## Tecnologías Usadas
- Python
- pandas
- Power BI
- SAP (pysap/sapnwrfc)
- Batch File / Apache Airflow

## Estructura del Proyecto
- **sap_integration/**: Scripts para extraer datos de SAP.
- **data_processing/**: Scripts para procesar y combinar los datos usando pandas.
- **powerbi/**: Archivos de Power BI para visualizaciones.
- **automation/**: Scripts de automatización (batch file o DAG de Airflow).
- **diagrams/**: Diagramas del flujo de trabajo.
- **data/**: Datos brutos y procesados.

## Instrucciones
1. **Clonar el Repositorio**
   ```bash
   git clone https://github.com/tu-usuario/automatizacion-sap-python.git
   cd automatizacion-sap-python
