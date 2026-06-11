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

You can now take a screenshot of the section and save it as `Task 3`.  

![Task 3](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%205/Tasks/Task%203.png?raw=true)  

## ***Task 4 - Create a task to transform the data in the txt file***  

Add the followng section below the `extract_data` section.  

```Python
transform_data = BashOperator(
    task_id="transform_data",
    bash_command=(
        "grep -v '^198\\.46\\.149\\.143$' "
        "/home/project/airflow/dags/capstone/extracted_data.txt "
        "> /home/project/airflow/dags/capstone/transformed_data.txt"
    ),
    dag=dag,
)
```

The underlying shell command is:  

```Bash
grep -v '^198\.46\.149\.143$' extracted_data.txt > transformed_data.txt
```

Inverts the search, so matching lines are excluded rather than printed. The pattern `^198\.46\.149\.143$` matches a line containing exactly that IP address.  

* `^` means the beginning of the line.
* `$` means the end of the line.
* `\.` treats each dot as a literal period rather than a regular-expression wildcard.

The redirection  

```Bash
> transformed_data.txt
```

writes the filtered results into the new file.  

Because the command is inside a Python string, each backslash is written twice:  

```Python
"^198\\.46\\.149\\.143$"
```

Python converts each `\\` into one literal backslash before Bash executes the command.  

You can take a screenshot of the section and save it as `Task 4`.  

![Task 4](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%205/Tasks/Task%204.png?raw=true)  

## ***Task 5 - Create a task to load the data***  

Add the following code underneath the existing `transform_data` task.  

```Python
load_data = BashOperator(
    task_id="load_data",
    bash_command=(
        "tar -cvf /home/project/airflow/dags/capstone/weblog.tar "
        "-C /home/project/airflow/dags/capstone transformed_data.txt"
    ),
    dag=dag,
)
```

The underlying Bash command is  

```Bash
tar -cvf /home/project/airflow/dags/capstone/weblog.tar \
-C /home/project/airflow/dags/capstone transformed_data.txt
```

`-c` creates a new archive, `-v` displays the file being archived, and `-f` specifies the archive filename. The option `-C /home/project/airflow/dags/capstone` tells `tar` to temporarily work inside the capstone directory before adding `transformed_data.txt`.  

You can now take a screenshot of this code section and save it as `Task 5`.  

![Task 5](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%205/Tasks/Task%205.png?raw=true)  

## ***Task 6 - Define the task pipeline***  

At the very bottom of `process_web_log.py` at this line, which ensures that Airflow extracts the IP addresses first, transforms the extracted data second, and creates the archive only after the transformation has completed successfully.  

```Python
extract_data >> transform_data >> load_data
```

You can take a picture of this section and save it as `Task 6`.  

![Task 6](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%205/Tasks/Task%206.png?raw=true)  

# ***Exercise 3 - Getting the DAG operational***  

Save `process_web_log.py` by clicking on `File > Save` on the upper ribbon (or, alternatively, click `Ctrl` + `S`).  

## ***Task 7 - Submit the DAG***  

After saving, to find the DAG in Airflow, run the command below.  

```Bash
airflow dags list | grep process_web_log
```

If the dags appear, it means it has been submitted correctly. 

You can take a screenshot of the output and save it as `Task 7`.  

![Task 7](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%205/Tasks/Task%207.png?raw=true)  

## ***Task 8 - Unpause the DAG***  

Before to unpause the dag, run the command below to have unrestricted access to the Dag folder. 

```Bash
chmod a+rwx /home/project/airflow/dags/capstone
```

Once done: 

1. Enter the Apache Airflow Webserverby clicking the dedicated button on the EDI
2. Locate process_web_log in the DAG list.
3. Find the toggle switch beside it.
4. Click the switch to activate the DAG.

You can take a screenshot of the unpaused DAG and save it as `Task 8`.  

![Task 8](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%205/Tasks/Task%208.png?raw=true)  

## ***Task 9 - Monitor the DAG***  

Open the DAG by clicking on its name. This opens the DAG details page. Trigger the DAG manually by clicking the "Play" button. You can run the DAG several times. 

Once satisfied, take a screenshot of the graph showing the success of all its activities and save it as `Task 9`.  

![Task 9](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%205/Tasks/Task%209.png?raw=true)
