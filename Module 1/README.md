![Skills_Network](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/images/image.png)  

<h1 align="center">Hands-on Lab: OLTP Database</h1>  

# ***Scenario***  

You are a data engineer at an e-commerce company. Your company needs you to design a data platform that uses MySQL as an OLTP database. You will be using MySQL to store the OLTP data.  

# ***Objectives***  

In this assignment you will:  

* design the schema for OLTP database.

* load data into OLTP database.

* automate admin tasks.

<h1 align="center">Exercises - Setting up the database</h1>  

# ***Exercise 1 - Check the lab environment***  

Before you proceed with the assignment:  

* Start MySQL server.

# ***Exercise 2 - Design the OLTP Database***  

## ***Task 1 - Create a database.***  

Create a database named `sales`.  

## **Task 2 - Design a table named `sales_data`.**  

Design a table named `sales_data` based on the sample data given.  

<div align="center">
  <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/oltp/sampledata.png" alt="sales_data">
</div>

> *Note: Ensure that the field names (i.e., column names) in your SQL statement for creating the table exactly match those shown in the screenshot above.*

Create the `sales_data` table in `sales` database.

Save the SQL statement used to create the table and its output in a text document for future reference.  

<h1 align="center">Exercises - Querying and Admin tasks</h1>  

# ***Exercise 3 - Load the Data***  

## ***Task 3 - Import `oltpdata.csv` into the `sales_data` table and write a SQL query to count the number of records in it.***  

Download the file oltpdata.csv from [here](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/oltp/oltpdata.csv).

Save the SQL statement you used and its output in a text document for future reference.  

# ***Exercise 4 - Set up Admin tasks***  

## ***Task 4 - Create an index***  

Create an index named `ts` on the `timestamp` field.  

## ***Task 5 - List indexes***  

List indexes on the table `sales_data`.

Save the SQL statement you used and its output in a text document for future reference.  

## ***Task 6 - Write a bash script to export data.***  

Write a bash script named `datadump.sh` that exports all the rows in the sales_data table to a file named `sales_data.sql`.

Save the contents of the `datadump.sh` bash file, the command you used, and the resulting output in a text document for future reference.  

# Author
# ***[Matteo Meloni](https://www.linkedin.com/in/matteo-meloni-40a357154/)***
