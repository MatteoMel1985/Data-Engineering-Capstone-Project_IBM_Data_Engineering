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

Take a screenshot of the output and name it `9-DimDate.png`
