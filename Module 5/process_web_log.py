```python
# Importing the required Python and Apache Airflow libraries

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


# Defining the default arguments applied to the DAG tasks

default_args = {
    "owner": "Artifex-Datorum",
    "start_date": datetime(2026, 6, 11),
    "email": ["your_email@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}


# Defining the daily web-log processing DAG

dag = DAG(
    dag_id="process_web_log",
    default_args=default_args,
    description="A daily pipeline that processes web server log data",
    schedule="@daily",
    catchup=False,
)


# Creating the task that extracts IP addresses from the web server log

extract_data = BashOperator(
    task_id="extract_data",
    bash_command=(
        "awk '{print $1}' "
        "/home/project/airflow/dags/capstone/accesslog.txt "
        "> /home/project/airflow/dags/capstone/extracted_data.txt"
    ),
    dag=dag,
)


# Creating the task that removes the specified IP address

transform_data = BashOperator(
    task_id="transform_data",
    bash_command=(
        "grep -v '^198\\.46\\.149\\.143$' "
        "/home/project/airflow/dags/capstone/extracted_data.txt "
        "> /home/project/airflow/dags/capstone/transformed_data.txt"
    ),
    dag=dag,
)


# Creating the task that archives the transformed data

load_data = BashOperator(
    task_id="load_data",
    bash_command=(
        "tar -cvf /home/project/airflow/dags/capstone/weblog.tar "
        "-C /home/project/airflow/dags/capstone transformed_data.txt"
    ),
    dag=dag,
)


# Defining the execution order of the pipeline tasks

extract_data >> transform_data >> load_data
```
