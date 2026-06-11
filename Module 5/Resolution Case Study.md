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

```Bash
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


