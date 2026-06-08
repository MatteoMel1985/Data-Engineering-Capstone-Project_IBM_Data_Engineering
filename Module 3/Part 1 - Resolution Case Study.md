# ***Exercise 1 - Design a Data Warehouse***  

## ***Task 1 - Design the dimension table `softcartDimDate`***  

Start the PostgreSQL server from the SN Toolbox as shown in the image below.  

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

Once the window is opened, name the database `softcart`, and click the `Save` button. Now

1. Select the `softcart` database.
2. Go to the top menu.
3. Click: `Tools > ERD Tool`

This opens the diagram editor where you can design the table visually. In the ERD tool, click the Add Table button (a small `+` icon in the top ribbon).

Name the table `softcartDimDate`. 

Do not click on the `Save` button yet. Proceed on the `Columns` tab, and click on the `+` icon on the top-right side of the window. 

Manually fill each column with the attributes and information below.

<div align="center">

| Column name | Data type | Length/Precision | Primary Key? |
| :---: | :---: | :---: | :---: |
| dateid | integer | | Yes | 
| date | date | | |  
| year | integer | |  
| quarter | integer| |  
| quartername | character varying | 2 | |  
| month | integer | |  
| monthname | character varying | 10 | |  
| day | integer | |  
| weekday | integer | |  
| weekdayname | character varying | 10 | |  

</div>  

Ensure that the attribute `dateid` is marked as Primary Key. Click on the `Save`

Now you can take a screenshot of the result and save it as `Task 1`.

![Task 1]([)](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%203/Part%201%20-%20Tasks/Task%201.png?raw=true)  

## ***Task 2 - Design the dimension table `softcartDimCategory`***  

Repeat the same procedure explained in Task 1, but save the table as `softcartDimCategory` and insert the values below. 

<div align="center">

| Column name | Data type | Length/Precision | Primary Key? |
| :---: | :---: | :---: | :---: |
| categoryid | integer | | Yes |
| category | character varying | 10 | |

</div>  

Take a screenshot of the result in your ERD and save it as `Task 2`.  

![Task 2](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%203/Part%201%20-%20Tasks/Task%202.png?raw=true)  

## ***Task 3 - Design the dimension table `softcartDimItem`***  

Repeat the same procedure explained in Task 1, but save the table as `softcartDimItem` and insert the values below.  

<div align="center">

| Column name | Data type | Length/Precision | Primary Key? |
| :---: | :---: | :---: | :---: |
| itemid | integer | | Yes |
| item | character varying | 10 | |

</div>  

Take a screenshot of the result in your ERD and save it as `Task 3`.

![Task 3](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%203/Part%201%20-%20Tasks/Task%203.png?raw=true)  

## ***Task 4 - Design the dimension table `softcartDimCountry`***  

Repeat the same procedure explained in Task 1, but save the table as `softcartDimCountry` and insert the values below.  

<div align="center">

| Column name | Data type | Length/Precision | Primary Key? |
| :---: | :---: | :---: | :---: |
| countryid | integer | | Yes |
| country | character varying | 100 | |

</div>  

Take a screenshot of the result in your ERD and save it as `Task 4`.  

![Task 4](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%203/Part%201%20-%20Tasks/Task%204.png?raw=true)  



