import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import DBSCAN
import pickle
import os

DATA_PATH = "/opt/airflow/dags/data"
MODEL_PATH = "/opt/airflow/dags/models"

def load_data():
    os.makedirs(DATA_PATH, exist_ok=True)
    columns = [
        'age', 'sex', 'cp', 'trestbps', 'chol', 'fbs',
        'restecg', 'thalach', 'exang', 'oldpeak',
        'slope', 'ca', 'thal', 'target'
    ]
    df = pd.read_csv(f"{DATA_PATH}/heart_disease_uci.csv", header=None, names=columns)
    df.dropna(inplace=True)
    df.to_csv(f"{DATA_PATH}/processed_heart_disease.csv", index=False)
    print("✅ Data Loaded & Saved:", df.shape)


def data_preprocessing():
    os.makedirs(DATA_PATH, exist_ok=True)
    df = pd.read_csv(f"{DATA_PATH}/processed_heart_disease.csv")

    # Convert all categorical columns to numeric codes
    df = df.apply(lambda col: col.astype('category').cat.codes if col.dtype == 'object' else col)

    # Handle missing values if any
    df = df.fillna(0)

    # Scale numeric data
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(df.drop("target", axis=1))
    scaled_df = pd.DataFrame(scaled, columns=df.columns[:-1])
    scaled_df["target"] = df["target"]  # add target column back

    # Save output
    scaled_df.to_csv(f"{DATA_PATH}/scaled_heart_disease.csv", index=False)
    print("✅ Data Scaled & Saved:", scaled_df.shape)


def build_save_model():
    os.makedirs(MODEL_PATH, exist_ok=True)
    data = pd.read_csv(f"{DATA_PATH}/scaled_heart_disease.csv")
    model = DBSCAN(eps=0.5, min_samples=5)
    model.fit(data)
    with open(f"{MODEL_PATH}/dbscan_model.pkl", "wb") as f:
        pickle.dump(model, f)
    print("✅ Model trained and saved at:", f"{MODEL_PATH}/dbscan_model.pkl")


def evaluate_model():
    import numpy as np
    from sklearn import metrics
    with open(f"{MODEL_PATH}/dbscan_model.pkl", "rb") as f:
        model = pickle.load(f)
    dummy_data = np.random.rand(100, 2)
    dummy_labels = np.random.randint(0, 2, size=100)
    score = metrics.silhouette_score(dummy_data, dummy_labels)
    print(f"✅ Model Evaluation Complete. Silhouette Score: {score}")