# Automating SAP Data Pipelines with Python and Power BI

## Description
This project automates the extraction of data from SAP, processes the data using pandas, visualizes it in Power BI, and automates the entire workflow using a batch file or Apache Airflow.

## Technologies Used
- **Python** 
- **SAP ECC** 
- **Power BI**
- **Windows Task Scheduler** / **Apache Airflow**

## Project Structure
```plaintext
├── Sap Integration   # Scripts for extracting data from SAP
├── Data Processing   # Scripts for processing and combining data using pandas
├── Power Bi          # Power BI files for visualizations
├── Automation        # Automation scripts (Batch file + Windows Task Scheduler or Airflow DAG)
├── Diagrams          # Workflow diagrams
└── Data              # Raw and processed data
