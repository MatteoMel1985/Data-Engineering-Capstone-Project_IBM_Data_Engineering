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

