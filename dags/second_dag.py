from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(0,0,0,0,0),
    'email': ['lianjjchina@hotmail.com'],
    'email_on_failure': False,
    "retries": 1
}

dag = DAG(
        dag_id="second_dag",
        default_args= default_args,
        schedule_interval=timedelta(days = 1),
)

def just_a_function():
    print("I'm going to show you something :)")

run_etl = PythonOperator(
    task_id='second_dag',
    python_callable=just_a_function,
    dag=dag,
)

run_etl