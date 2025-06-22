# NYC Taxi Data Analysis with Apache Spark

## Overview
This project demonstrates large-scale data processing capabilities using Apache Spark, processing NYC Taxi trip data to derive meaningful insights. The implementation includes container orchestration with Kubernetes and workflow management with Apache Airflow.

## Project Structure
```
nyc-taxi-spark-analysis/
├── data/
│   ├── raw/          # Raw data files (not in git)
│   ├── processed/    # Processed data files (not in git)
│   └── sample/       # Sample datasets for testing
├── src/
│   ├── spark/        # Spark processing scripts
│   └── airflow/      # Airflow DAGs
├── scripts/          # Utility scripts
├── notebooks/        # Jupyter notebooks
├── tests/           # Unit tests
├── docs/            # Documentation
├── kubernetes/      # K8s configuration files
└── docker/         # Docker configuration files
```

## Setup
1. Clone the repository
```bash
git clone https://github.com/nicoinuggi/nyc-taxi-spark-analysis.git
cd nyc-taxi-spark-analysis
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Data
This project uses the NYC Taxi & Limousine Commission trip record data. 
- Source: [NYC TLC Trip Record Data](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- A sample dataset is provided in the `data/sample/` directory
- For full analysis, run the data download script:
```bash
python scripts/download_data.py
```

## Usage
[To be added as project develops]



## License
[MIT](https://choosealicense.com/licenses/mit/)
