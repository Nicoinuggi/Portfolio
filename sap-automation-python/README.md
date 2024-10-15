# Automating SAP Data Pipelines with Python and Power BI

## Description
This project automates the extraction of data from SAP, processes the data using pandas, visualizes it in Power BI, and automates the entire workflow using a batch file with Windos Task Scheduler or Apache Airflow.

## Technologies Used
- **Python** 
- **SAP Logon/GUI/ECC** 
- **Power BI**
- **Windows Task Scheduler** / **Apache Airflow**

## Project Structure
```plaintext
├── Sap Integration   # Script for connecting to and extracting data from SAP
├── Data Processing   # Scripts for processing and combining data using Pandas lib
├── Power Bi          # Power BI  for visualizations
├── Automation        # Automation scripts (Batch file + Windows Task Scheduler or Airflow DAG)
├── Diagrams          # Workflow diagrams
└── Data              # Raw and processed data
