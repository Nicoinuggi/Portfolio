# Automating SAP Data Pipelines with Python and Power BI
![image](https://github.com/user-attachments/assets/939599bc-a210-44be-b930-124fda786ae6)

## Description
This project automates the extraction of data from SAP, processes the data using pandas lib, visualizes it in Power BI, and automates the entire workflow using Apache Airflow or a batch file with Windows Task Scheduler for a simpler approach. Specific case examples are not included. Instead, a general template is provided for users to adapt to their specific needs. 

## Technologies Used
- **Python** 
- **SAP Logon/GUI/ECC** 
- **Power BI**
- **Windows Task Scheduler** / **Apache Airflow**

## Project Structure
```plaintext
├── Sap integration   # Script for connecting to and extracting data from SAP
├── Data Processing   # Scripts for processing and combining data using Pandas lib
├── Power Bi          # Power BI  for visualizations
├── Automation        # Automation scripts ( Airflow DAG or Batch file + Windows Task Scheduler or)
├── Diagrams          # Workflow diagrams
└── Data              # Raw and processed data
