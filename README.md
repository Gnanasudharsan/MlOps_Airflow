# MlOps_Airflow

# Airflow Lab 1 – Heart Disease Clustering (DBSCAN)

This project implements an **Apache Airflow pipeline** for automating an end-to-end **data processing and unsupervised machine learning workflow**.  
The DAG performs **ETL, preprocessing, DBSCAN clustering, and model evaluation** on the **UCI Heart Disease dataset** using Airflow’s task orchestration capabilities.

---

## 🎯 Objective
To build a modular, automated pipeline in Airflow that:
1. Loads and cleans the heart disease dataset  
2. Scales and encodes data for clustering  
3. Builds and saves a **DBSCAN clustering model**  
4. Evaluates model quality using the **Silhouette Score**

---

## ⚙️ Airflow DAG Overview
The DAG is named **`Airflow_Lab1_HeartDisease`** and includes the following tasks:

| Task | Description | Output |
|------|--------------|--------|
| **load_data** | Loads the UCI Heart Disease dataset and drops null values | `processed_heart_disease.csv` |
| **data_preprocessing** | Encodes categorical features and scales numerical features using `MinMaxScaler` | `scaled_heart_disease.csv` |
| **build_save_model** | Builds a **DBSCAN** clustering model and saves it using `pickle` | `dbscan_model.pkl` |
| **evaluate_model** | Evaluates clustering quality using **Silhouette Score** | Printed in logs |

Each task runs as an **independent PythonOperator** inside Airflow.

---

## 🧠 ML Model Used – DBSCAN
- **Model:** Density-Based Spatial Clustering of Applications with Noise (DBSCAN)  
- **Reason:** Unlike K-Means, DBSCAN doesn’t require specifying the number of clusters. It’s effective for irregular, non-spherical data distributions.  
- **Evaluation Metric:** Silhouette Score (higher = better cluster separation)

---

## 🧰 Prerequisites
Before running the project, ensure you have:
- Docker Desktop (≥ 4 GB memory allocated)
- Git
- Internet access to pull the Airflow image

Python libraries (installed inside the container):
```bash
pandas
scikit-learn
pickle
numpy
apache-airflow==2.5.1

```
⸻

🚀 Setup and Execution

1️⃣ Clone the Repository
``` bash
git clone https://github.com/Gnanasudharsan/MlOps_Airflow.git
cd MlOps_Airflow
```
2️⃣ Start Airflow in Docker
``` bash
docker compose up -d
```
Wait until you see the message:
```bash
airflow-webserver | 127.0.0.1 - - "GET /health HTTP/1.1" 200 -
```
3️⃣ Access Airflow UI

Visit http://localhost:8080
Login using:
``` bash
Username: airflow
Password: airflow
```
4️⃣ Trigger the DAG
	•	Go to DAGs → Airflow_Lab1_HeartDisease
	•	Turn it ON
	•	Click Trigger DAG
	•	Monitor progress under the Graph View

When successful, all tasks will appear green ✅:
``` bash
load_data → data_preprocessing → build_save_model → evaluate_model
```

⸻

📊 Output Files

After successful DAG run:

File	Location	Description
processed_heart_disease.csv	/opt/airflow/dags/data	Cleaned dataset
scaled_heart_disease.csv	/opt/airflow/dags/data	Normalized dataset
dbscan_model.pkl	/opt/airflow/dags/models	Trained DBSCAN model

You can verify via Docker:
``` bash
docker exec -it lab_1-airflow-webserver-1 bash
ls /opt/airflow/dags/data
ls /opt/airflow/dags/models
```

⸻

🧩 Key Learnings
	•	Automated end-to-end ML workflow using Airflow DAGs
	•	Data preprocessing with scaling and encoding
	•	Clustering with DBSCAN and model persistence using Pickle
	•	Integration of ML lifecycle within containerized Airflow setup

⸻

🧱 References
	•	Apache Airflow Documentation
	•	UCI Heart Disease Dataset
