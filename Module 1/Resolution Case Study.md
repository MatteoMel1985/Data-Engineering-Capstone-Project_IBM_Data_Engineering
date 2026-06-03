# ***Exercise 1 - Check the lab environment***  

Start MySQL by going on 

> *Skills Network Toolbox > DATABASES > MySQL*

And click on the button `Create`.

<div align="center">
  <img src="https://github.com/MatteoMel1985/Relational-Dataset-Images/blob/main/Images/Capstone_Screenshot1.png?raw=true" alt="sales_data">
</div>

# ***Exercise 2 - Design the OLTP Database***  

## ***Task 1 - Create a database.*** 

Once MySQL is active, click below on `Connection Information`, and scroll down until you find `MySQL CLI Command`. Copy it and run it from your terminal.

**NOTE**:  Attention, the host, port, and password might vary according to your version of MySQL. Ensure to use the password you find on our MySQL.

```Bash
mysql --host=172.21.28.168 --port=3306 --user=root --password=1gBL8r59FqUAoiaQV6NZ2mFy
```

Once done, your terminal should appear as follows:

```Bash
mysql>
```

Once ready, run the command below to create the database.

```SQL
CREATE DATABASE sales;
```

You can now take a screenshot of the result and save it as `Task 1`.  

![Task 1](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%201/Tasks/Task%201.png?raw=true)  

## **Task 2 - Design a table named `sales_data`**  

If the database was created correctly, you should see this output in the terminal. 

```Bash
Query OK, 1 row affected (0.01 sec)
```

To create the table named `sales_data` with the attributes shown in [Task 2](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%201/README.md#task-2---design-a-table-named-sales_data), inside the database `sales`, first select the database by running this command.

```SQL
USE sales;
``` 

If run correctly, you should see `Database changed` in the terminal. To create the table, write the following statement. 

```SQL
CREATE TABLE sales_data (
    product_id INT,
    customer_id INT,
    price INT,
    quantity INT,
    `timestamp` DATETIME
);
```

If run successfully, the terminal will show a similar output: `Query OK, 0 rows affected (0.03 sec)`.  

You can now take a screenshot of the result and save it as `Task 2`.

![Task 2](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%201/Tasks/Task%202.png?raw=true)

# ***Exercise 3 - Load the Data***  

## ***Task 3 - Import `oltpdata.csv` into the `sales_data` table and write a SQL query to count the number of records in it.***  

To import `oltpdata.csv` into the `sales_data` table, we will first have to exit the MySQL CLI, and to do so, we simply must run the command

```SQL
exit
```

Now, we can proceed with downloading `oltpdata.csv` by running the command below.

```Bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/oltp/oltpdata.csv
```

By default, the file will be saved in the path `/home/project`. To verify it was saved in this path, run the command below.

```Bash
ls -l /home/project/oltpdata.csv
``` 

`ls` stands for list, whereas `-l` stands for "long listing format". 

 Once ensure the file is in `/home/project`, we'll have to connect again with the MySQL CLI. As before, ensure to insert your  host, port, and password. 

```Bash
mysql --local-infile=1 --host=172.21.28.168 --port=3306 --user=root --password=INSERT_YOUR_PASSWORD sales
```

`--local-infile=1` enables the ability to load data from a local file directly into a MySQL tabl; whereas `sales` indicates the databes where we want to load the file. 

Once run, the terminal should appear as follows. 

```Bash
mysql>
```

Now run  

```SQL
USE sales;
```

And immediately after, load the file in the database with the command below.

```SQL
LOAD DATA LOCAL INFILE '/home/project/oltpdata.csv'
INTO TABLE sales_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
```

If loaded correcty, the output should show something similar:

```Bash
Query OK, 2604 rows affected (0.04 sec)
Records: 2604  Deleted: 0  Skipped: 0  Warnings: 0
```

You can now take a screenshot of the result and save it as `Task 3`. 

![Task 3](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%201/Tasks/Task%203.png?raw=true)

# ***Exercise 4 - Set up Admin tasks***  

## ***Task 4 - Create an index***  

Ensure you are inside the `sales` database by running the command below. 

```SQL
USE sales;
```

Finally, to create the index `ts` on the column `timestamp`, you can run the statemenet below. I reccomend using backticks because `timestamp` is also a MySQL keyword/data type.  

```SQL
CREATE INDEX ts ON sales_data (`timestamp`);
```

You can take a screenshot of the result and save it as `Task 4`.

![Task 4](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%201/Tasks/Task%204.png?raw=true)  

## ***Task 5 - List indexes***  

To verify that the index was correctly created, run the code below.

```SQL
SHOW INDEX FROM sales_data;
```

You should see a row where.

```Bash
Key_name = ts
Column_name = timestamp
```

Take the screenshot of the result and save it as `Task 5`.  

![Task 5](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%201/Tasks/Task%205.png?raw=true)  

## ***Task 6 - Write a bash script to export data***  

To write the Bash script, we must exit the MySQL CLI by running the command below in the terminal. 

```SQL
exit
```

To create the file, write the following command.  

```Bash
nano datadump.sh
```

Inside the file, write the code below (ensure to replace correctly the host, the port, and the password with those found on your MySQL.  

```Bash
#!/bin/bash

mysqldump --host=172.21.51.80 --port=3306 --user=root --password=INSERT_YOUR_PASSWORD sales sales_data > sales_data.sql
```

Save it by pressing simultaneously `CTRL` + `O`, then `Enter`, and `CTRL` + `X`.  

The command exports the table `sales_dat`a from the database sales into a file named `sales_data.sql`.  Once saved, you will be able to see it in the Explorer pane of your EDI.  

To make it executable, run the command below from your terminal.  

```Bash
chmod +x datadump.sh
```

`+x` adds execute permission to the file.  

Finally, you can run the script by typing on the terminal.  

```Bash
./datadump.sh
```

If you have done everything correctly, the file [sales_data.sql](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%201/sales_data.sql) will be downloaded and visible in your Explorer pane.  

Below is a screenshot of the Bash script, which I saved for the completion of `Task 6`.  

![Task 6](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%201/Tasks/Task%206.png)



