from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 10, 18),
    'depends_on_past': False,
}

dag = DAG(
    'my_etl_dag',
    default_args=default_args,
    schedule_interval='@once',
    tags=['example'],
)

spark_job = SparkSubmitOperator(
    task_id='run_etl',
    application='/opt/airflow/spark_jobs/etl_job.py',  # Путь до вашего Spark script
    name='run_etl_job',
    conn_id='spark_default',
    dag=dag,
)

spark_job
