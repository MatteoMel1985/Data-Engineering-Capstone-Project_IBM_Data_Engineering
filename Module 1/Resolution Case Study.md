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


