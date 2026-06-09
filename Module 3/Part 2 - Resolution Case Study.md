# ***Prepare the lab environment***  

Start the PostgreSQL server as shown in the image below.  

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/xTYj5eYM4bLg7oV0HHGxBA/DWF1.png" width="60%">

Open the pgAdmin Graphical User Interface by clicking the pgAdmin launch button in the Cloud IDE interface.  

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/fUYB2aGP-Xg8FIX8hA8Yrw/DWF2.png" width="60%">

Once the pgAdmin GUI opens, click on the Servers tab on the left side of the page. You will be prompted to enter a password.  

![password_request](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/BIWorkaroundFiles/week2/images/2.png)  

To retrieve your password, click on the PostgreSQL and go to Conection Information tab on the top of the interface.  

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/V46jb0XRCMzh6nnTGmsJFQ/DWF3.png" width="60%">

Scroll down to the session password and click on the Copy icon to the right of your password to copy onto your clipboard.  

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/EVui_ox9j9mK7dKeDKjtAQ/DWF4.png" width="60%">

Navigate back to the pgAdmin tab and paste in your password, then click OK.  

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/BIWorkaroundFiles/week2/images/2.2.png" width="100%">

You will then be able to access the pgAdmin GUI tool.

In the left tree-view, right-click on `Databases > Create > Database`.   

<img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/BIWorkaroundFiles/week2/images/3.png" width="100%">

Once the window is opened, name the database `Test1`, and click the `Save` button. Now  

1. Select the `Test1` database.
2. Go to the top menu.
3. Click: Tools > Query Tool

This opens the diagram editor where you can design the table visually. In the ERD tool, click the Open File button (a small folder icon in the top ribbon). Once the window opens, it should be set by default on the path `/home/`. That is not suitable for uploading the file [CREATE_SCRIPT.sql](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%203/Part%202%20-%20Script%20and%20CSVs/CREATE_SCRIPT.sql). To do so, ensure to navigate on the path `/var/lib/pgadmin/`. Once there, click on the three-dot icon on the upper right of the window and select `Upload`.  

![Screenshot_3](https://raw.githubusercontent.com/MatteoMel1985/Relational-Dataset-Images/2d9f7a02822edb250d639296a849b4ce9cf0316a/Data%20Warehouse/Screenshot_3.PNG)  

Drag and drop the file `CREATE_SCRIPT.sql` and, once uploaded, click on the highlighted small `x` icon. 

![Screenshot_4](https://github.com/MatteoMel1985/Relational-Dataset-Images/blob/main/Data%20Warehouse/Screenshot_4.PNG?raw=true)  

Finally, highlight the file `CREATE_SCRIPT.sql`, and click on the `Select` button on the bottom-right corner of the window. You can now run the script and take a screenshot of it.  

![Prepare the lab](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%203/Part%202%20-%20Tasks/Prepare%20the%20lab.png?raw=true)  

## ***Task 1 - Load data into the dimension table DimDate***   

In the left panel of pgAdmin, expand

```
Servers > PostgreSQL > Databases > Test1 > Schemas > public > Tables
```

There, you will find the table `DimDate1`. Right-click on it and select `Import/Export Data...`.   Click on the folder on the right side of `Filename`. 

![Screenshot_1](https://github.com/MatteoMel1985/Relational-Dataset-Images/blob/main/Data%20Warehouse/Screenshot_1.PNG?raw=true)  

Click on the upward pointing arrow on the upper left side of the window and select the following path: `/var/lib/pgadmin/`.  

![Screenshot_2](https://github.com/MatteoMel1985/Relational-Dataset-Images/blob/main/Data%20Warehouse/Screenshot_2.PNG?raw=true)  

Click on the three-dot icon on the upper right of the window.  

![Screenshot_3](https://raw.githubusercontent.com/MatteoMel1985/Relational-Dataset-Images/2d9f7a02822edb250d639296a849b4ce9cf0316a/Data%20Warehouse/Screenshot_3.PNG)  

Drag and drop the file `DimDate.csv` and, once uploaded, click on the highlighted small `x` icon. 

![Screenshot_4](https://github.com/MatteoMel1985/Relational-Dataset-Images/blob/main/Data%20Warehouse/Screenshot_4.PNG?raw=true)  

Choose the `DimDate.csv` file on the screen and click the button `Select` on the lower-right corner of the window. 

![Select](https://github.com/MatteoMel1985/Relational-Dataset-Images/blob/main/Data%20Warehouse/03.09.04-DimDate.png?raw=true)

Click on `Options`, select `Header`, and click on the lower-right button `OK`.  

![Screenshot_5](https://github.com/MatteoMel1985/Relational-Dataset-Images/blob/main/Data%20Warehouse/Screenshot_5.PNG?raw=true)

Now the table is populated. 

Now run the following SQL query from the query tool.

```SQL
SELECT *
FROM "DimDate"
LIMIT 5;
```

Take a screenshot of the output and name it `Task 1`.  

![Task 1](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%203/Part%202%20-%20Tasks/Task%201.png?raw=true)

## ***Task 2 - Load data into the dimension table DimCategory***   

Repeat the same procedure explained in Task 1, but with the table `DimCategory`. Run the SQL query below.

```SQL
SELECT *
FROM "DimCategory"
LIMIT 5;
```

Take a screenshot of the output and name it `Task 2`.  

![Task 2](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%203/Part%202%20-%20Tasks/Task%202.png?raw=true)  

## ***Task 3 - Load data into the dimension table DimCountry***   

Repeat the same procedure explained in Task 1, but with the table `DimCountry`. Run the SQL query below.  

```SQL
SELECT *
FROM "DimCountry"
LIMIT 5;
```

Take a screenshot of the output and name it `Task 3`.  

![Task 3](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%203/Part%202%20-%20Tasks/Task%203.png?raw=true)  

## ***Task 4 - Load data into the fact table FactSales***   

Repeat the same procedure explained in Task 1, but with the table `FactSales`. Run the SQL query below.  

```SQL
SELECT *
FROM "FactSales"
LIMIT 5;
```

Take a screenshot of the output and name it `Task 4`.  

![Task 4](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%203/Part%202%20-%20Tasks/Task%204.png?raw=true)  

## ***Task 5 - Create a grouping sets query***   

A grouping set allows you to calculate multiple levels of aggregation in one query. For example, instead of writing separate queries for 'Total sales by country and category', `Total sales by country only`, `Total sales by category only`, and `Grand total sales`, we can calculate all of them together using `GROUP BY GROUPING SETS (...)`.

The grouping sets below use the columns `country`, `category`, and `totalsales.`  

```SQL
SELECT 
    TRIM(c.country) AS country,
    TRIM(cat.category) AS category,
    SUM(f.amount) AS totalsales
FROM "FactSales" f
JOIN "DimCountry" c
    ON f.countryid = c.countryid
JOIN "DimCategory" cat
    ON f.categoryid = cat.categoryid
GROUP BY GROUPING SETS (
    (c.country, cat.category),
    (c.country),
    (cat.category),
    ()
)
ORDER BY 
    country,
    category;
```

Once run, you can take a screenshot of it and save it as `Task 5`.  

![Task 5](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%203/Part%202%20-%20Tasks/Task%205.png?raw=true)  

## ***Task 6 - Create a rollup query***   

A rollup query creates hierarchical totals. If you group by `ROLLUP(year, country)`, PostgreSQL calculates: `Sales by year and country`, `Sales by year only`, and `Grand total`. So, unlike grouping sets, where you manually choose each grouping combination, rollup automatically follows a hierarchy from left to right.  

The rollup below use the columns `year`, `country`, and `totalsales`.  

```SQL
SELECT
    d.year,
    TRIM(c.country) AS country,
    SUM(f.amount) AS totalsales
FROM "FactSales" f
JOIN "DimDate" d
    ON f.dateid = d.dateid
JOIN "DimCountry" c
    ON f.countryid = c.countryid
GROUP BY ROLLUP(d.year, c.country)
ORDER BY
    d.year,
    c.country;
```

Once run, you can take a screenshot of it and save it as `Task 6`.  

![Task 6](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%203/Part%202%20-%20Tasks/Task%206.png?raw=true)  

## ***Task 7 - Create a cube query***   

A cube query creates aggregations for all possible combinations of the selected grouping columns. If you write `GROUP BY CUBE(year, country)`, PostgreSQL calculates `Average sales by year and country`, `Average sales by year only`, `Average sales by country only`, and `Overall average sales`; so, while `ROLLUP(year, country)` follows a hierarchy, `CUBE(year, country)` gives every possible subtotal combination.  

The cube query below use the columns `year`, `country`, and `average sales`.  

```SQL
SELECT
    d.year,
    TRIM(c.country) AS country,
    AVG(f.amount) AS averagesales
FROM "FactSales" f
JOIN "DimDate" d
    ON f.dateid = d.dateid
JOIN "DimCountry" c
    ON f.countryid = c.countryid
GROUP BY CUBE(d.year, c.country)
ORDER BY
    d.year,
    c.country;
```

Once run, you can take a screenshot of it and save it as `Task 7`.  

![Task 7](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%203/Part%202%20-%20Tasks/Task%207.png?raw=true)  

## ***Task 8 - Create an MQT***   
