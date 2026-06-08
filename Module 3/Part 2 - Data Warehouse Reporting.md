![Skills_Network](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/images/image.png)  

<h1 align="center">Hands-on Lab:Data Warehouse Reporting</h1>  

# ***Prepare the lab environment***  

Before you start the assignment:

1. Right Click on this [link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/nm75oOK5n7AGME1F7_OIQg/CREATE-SCRIPT.sql) and save this SQL file in you local system.

2. Start PostgreSQL server

3. Create a new database Test1

4. Create the following tables  
        
   * DimDate
   * DimCategory
   * DimCountry
   * FactSales

> After completing each task, save both the executed commands and their corresponding outputs in a text document, or take screenshots—depending on the option you have chosen. This information will be required to answer questions during the final project submission.

# ***Loading Data***  

In this exercise you will load the data into the tables. You will load the data provided by the company in csv format.  

## ***Task 1 - Load data into the dimension table DimDate***  

* Download the data from this [link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/data/DimDate.csv)  

* Load the downloaded data into DimDate table.

* Write a SQL query to display the first 5 rows of the table.

* Save the SQL statement you executed and its output in a text document, or take a screenshot of both for future reference.


## ***Task 2 - Load data into the dimension table DimCategory***  

* Download the data from this [link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/DimCategory.csv)

* Load the downloaded data into DimCategory table.

* Write a SQL query to display the first 5 rows of the table.

* Save the SQL statement you executed and its output in a text document, or take a screenshot of both for future reference.

## ***Task 3 - Load data into the dimension table DimCountry***  

* Download the data from this [link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/DimCountry.csv)

* Load the downloaded data into DimCountry table.

* Write a SQL query to display the first 5 rows of the table.

* Save the SQL statement you executed and its output in a text document, or take a screenshot of both for future reference.

## ***Task 4 - Load data into the fact table FactSales***  

* Download the data from this [link](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/datawarehousing/FactSales.csv)

* Load this data into FactSales table.

* Write a SQL query to display the first 5 rows of the table.

* Save the SQL statement you executed and its output in a text document, or take a screenshot of both for future reference.

# ***Queries for data analytics***  

In this exercise you will query the data you have loaded in the previous exercise.  

## ***Task 5 - Create a grouping sets query***  

* Create a grouping sets query using the columns country, category, totalsales.

* Save the SQL statement you executed and its output in a text document, or take a screenshot of both for future reference.

## ***Task 6 - Create a rollup query***  

* Create a rollup query using the columns year, country, and totalsales.

* Save the SQL statement you executed and its output in a text document, or take a screenshot of both for future reference

## ***Task 7 - Create a cube query***  

* Create a cube query using the columns year, country, and average sales.

* Save the SQL statement you executed and its output in a text document, or take a screenshot of both for future reference.

## ***Task 8 - Create an MQT***  

* Create an MQT named total_sales_per_country that has the columns country and total_sales.

* Save the SQL statement you executed and its output in a text document, or take a screenshot of both for future reference

End of the assignment.  

# Author
# ***[Matteo Meloni](https://www.linkedin.com/in/matteo-meloni-40a357154/)***
