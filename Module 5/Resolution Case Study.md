# ***Exercise 1 - Prepare the lab environment***  

Start Apache Airflow by following this path on your left pane:  

`Skills Network Toolbox > BIG DATA > Apache Airflow > Create`  

And wait until the database is active (it is often long and it might take a few minutes). 

If it doesn't appear on your EDI, open a terminal by going on the upper Ribbon Menu and select `Terminal > New Terminal` and run the command below.  

```Bash
mkdir -p /home/project/airflow/dags/capstone
```

The `-p` option creates the entire directory path if any part of it does not yet exist. It also avoids an error if the directory already exists. Now, move in the directory by running this command

```Bash
cd /home/project/airflow/dags/capstone
```

To confirm your location, run the command

```Bash
pwd
```

And expect the output `/home/project/airflow/dags/capstone`.

To download the file `accesslog.txt` directly in the path `/home/project/airflow/dags/capstone`, run the command below.  

```Bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/ETL/accesslog.txt
```

To confirm its download, you can list the contents of the directory by running the command below. 

```Bash
ls -lh /home/project/airflow/dags/capstone
```

In the output you should see `accesslog.txt`.

You can take a screenshot of the lab environment and save it as `Exercise 1`.  

![Exercise 1](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%205/Tasks/Exercise%20%201.png?raw=true)

# ***Exercise 2 - Create a DAG***  

## ***Task 1 - Define the DAG arguments***  

First, we will create the file `process_web_log.py` by running the command below.  

```Bash
touch process_web_log.py
```

Once appearing in the left pane of the EDI, double click the file, so as to script it from the editor pane, on top of the terminal. Add the following code.  

```Python
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    "owner": "Artifex-Datorum",
    "start_date": datetime(2026, 6, 11),
    "email": ["your_email@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}
```

If desired, replace `your_email@example.com` with your actual address, and `owner` with your name.  

Take a screenshot of the code you have written and save it as `Task 1`.

![Task 1](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%205/Tasks/Task%201.png?raw=true)  


## ***Task 2 - Define the DAG***  

Add the followng section below the DAG arguments.

```Python
dag = DAG(
    dag_id="process_web_log",
    default_args=default_args,
    description="A daily pipeline that processes web server log data",
    schedule="@daily",
    catchup=False,
)
```

The following line assigns the required name to the DAG.

```Python
dag_id="process_web_log"
```

This connects the DAG to the arguments defined in Task 1:

```Python
default_args=default_args
```

This provides a suitable description:

```Python
description="A daily pipeline that processes web server log data"
```

This schedules the DAG to run once per day:

```Python
schedule="@daily"
```

Finally, the line below prevents Airflow from automatically creating historical DAG runs for every missed daily interval between the `start_date` and the present date. This is useful in a lab because it avoids generating many unnecessary runs.  

```Python
catchup=False
```

You can take a screenshot of the section and save it as `Task 2`. 

![Task 2](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%205/Tasks/Task%202.png?raw=true)  

## ***Task 3 - Create a task to extract data***  

Add the followng section below the `process_web_log` section.  

```Python
extract_data = BashOperator(
    task_id="extract_data",
    bash_command=(
        "awk '{print $1}' "
        "/home/project/airflow/dags/capstone/accesslog.txt "
        "> /home/project/airflow/dags/capstone/extracted_data.txt"
    ),
    dag=dag,
)
```

The central shell command is:  

```Bash
awk '{print $1}' accesslog.txt > extracted_data.txt
```

which prints only that first field from every line.  

The redirection operator

```Bash
>
```

writes the output into `extracted_data.txt`.  

The task name is defined here

```Python
task_id="extract_data"
```

This is the name that will appear in the Airflow interface, whereas the shell operation executed by Airflow is defined by `bash_command=...`. The task is associated with your DAG using `dag=dag`.

