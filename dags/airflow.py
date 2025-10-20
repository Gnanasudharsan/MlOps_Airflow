from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from src.lab import load_data, data_preprocessing, build_save_model, evaluate_model

default_args = {
    'owner': 'gnanasudharsan',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=3)
}

with DAG(
    dag_id='Airflow_Lab1_HeartDisease',
    default_args=default_args,
    description='Heart Disease DBSCAN Clustering + Evaluation',
    schedule_interval='@daily',
    start_date=datetime(2025, 10, 20),
    catchup=False,
    tags=['heart_disease', 'DBSCAN', 'clustering']
) as dag:

    load_data_task = PythonOperator(
        task_id='load_data',
        python_callable=load_data
    )

    preprocess_task = PythonOperator(
        task_id='data_preprocessing',
        python_callable=data_preprocessing
    )

    build_model_task = PythonOperator(
        task_id='build_save_model',
        python_callable=build_save_model
    )

    evaluate_task = PythonOperator(
        task_id='evaluate_model',
        python_callable=evaluate_model
    )

    # Define DAG flow
    load_data_task >> preprocess_task >> build_model_task >> evaluate_task