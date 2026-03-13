# API Ingestion Pipeline

A Python backend service that collects data from multiple public APIs, cleans and validates the data, and stores normalized results for further analysis.

This project demonstrates how backend systems ingest, process, and store external data in real-world data pipelines.

---

# Project Goals

This project shows how to:

• Fetch data from multiple APIs  
• Parse and work with JSON responses  
• Clean and normalize different data formats  
• Validate incoming data  
• Handle API failures and errors  
• Store processed data for later analysis  

---

# Example Data Sources

The pipeline will collect data from multiple APIs such as:

• Weather API  
• Currency Exchange API  
• Country / Location API  

Example flow:

```
Weather API
Currency API
Country API
      ↓
Python Data Pipeline
      ↓
Data Cleaning + Validation
      ↓
Database / File Storage
```

---

# Tech Stack

Python libraries used in this project:

• Python 3  
• requests (API calls)  
• pydantic (data validation)  
• SQLite (data storage)  
• pytest (testing)  
• logging (system monitoring)

---

# Planned Features

• Fetch data from multiple APIs  
• Normalize responses into one schema  
• Skip invalid or corrupted data  
• Store cleaned data into a database  
• Log API failures and errors  
• Export processed data

---

# Project Structure (Planned)

```
api-ingestion-pipeline
│
├── app
│   ├── api_clients
│   ├── models
│   ├── services
│   └── utils
│
├── tests
├── data
├── logs
├── requirements.txt
└── README.md
```

---

# Setup

Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/api-ingestion-pipeline.git
cd api-ingestion-pipeline
```

Create virtual environment:

```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Run the Project

```
python app/main.py
```

---

# Future Improvements

• Add Docker support  
• Add API retry mechanisms  
• Add monitoring and metrics  
• Add automated tests  

---

# Author

Vivin Anitha Thambidurai  
MSc Advanced Computer Science  
University of Sheffield
