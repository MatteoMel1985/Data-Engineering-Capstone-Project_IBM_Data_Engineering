# ***Exercise 1 - Load data into Google Looker Studio***  

In this first exercise, we have to upload the file `ecommerce.csv` into Looker Studio and verify that the data has been loaded correctly.  

## ***Task 1 - Import data***  

Open Google Looker Studio in your browser.  

Then proceed as follows:  

1. Click **Create**.  
2. Select **Data source**.  
3. Choose the **File Upload** connector.  
4. Click **Upload files**.  
5. Select the file `ecommerce.csv` from your computer.  
6. Wait until Looker Studio finishes uploading and processing the file.  
7. When the dataset is visible and the file appears to be loaded successfully, take a screenshot.  

The screenshot for this task should show that the file `ecommerce.csv` has been successfully loaded into Looker Studio.  

You can now save the screenshot as `Task 1.png`.  

![Task 1](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%204/Tasks/Task%201.png?raw=true) 

## ***Task 2 - List first 10 rows***  

After importing the CSV file, Looker Studio will show the fields detected from the dataset. However, the task asks us to list the first 10 rows of the table.  

To do so, create a simple table in the report:  

1. From the data source page, click **Create report** or **Add to report**.  
2. Once the report opens, click **Insert**.  
3. Select **Table**.  
4. Place the table on the report canvas.  
5. In the chart setup panel, add the dataset fields that allow the first records to be displayed clearly.  
6. Set the number of rows to **10**, if Looker Studio gives you the option to control the row limit.  
7. Make sure the table displays the first ten rows of the uploaded data.  

A good table for the screenshot should include several meaningful fields, such as the date/order field, category field, product field, quantity field, and sales/price field, depending on the exact column names displayed by Looker Studio.  

You can now take a screenshot and save it as `Task 2.png`.  

![Task 2](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%204/Tasks/Task%202.png?raw=true)

# ***Exercise 2 - Accessing the Data Source in Google Looker Studio***  

## ***Task 3 - Create a data source***  

In this task, we simply need to show that the uploaded CSV file is now available as a Looker Studio data source.  

If you are still inside the report, you can access the data source from the right panel or from the menu:  

1. Click **Resource**.  
2. Select **Manage added data sources**.  
3. Find the data source created from `ecommerce.csv`.  
4. Click **Edit**, if needed, to open the data source schema.  
5. Verify that the fields from the CSV file are visible.  

The screenshot should show the created data source and its fields.  

You can now save the screenshot as `Task 3.png`.

![Task 3](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%204/Tasks/Task%203.png?raw=true)

# ***Exercise 3 - Create a dashboard***  

In this exercise, we create the three required dashboard charts.  

## ***Task 4 - Create a line chart***  

The first chart must show **month-wise total sales for the year 2020**.  

To create it:  

1. Open your Looker Studio report.  
2. Click **Insert**.  
3. Select **Line chart** or **Time series chart**.  
4. Place the chart on the report canvas.  
5. In the chart setup panel, configure the chart as follows:  

| Setting | Suggested value |
|---|---|
| Chart type | Line chart or Time series chart |
| Dimension | Month or Date |
| Metric | Total Sales / Sales / Amount |
| Aggregation | SUM |
| Filter | Year = 2020 |
| Sort | Month ascending |

If the chart uses the full date field instead of the month field, make sure the chart groups the data by month.  

If you need to create the filter manually:  

1. Go to the chart setup panel.  
2. Click **Add a filter**.  
3. Create a filter named `Year 2020`.  
4. Include records where `Year` equals `2020`.  
5. Apply the filter to the line chart.  

The final result should be a line chart with months on the horizontal axis and total sales on the vertical axis.  

You can now take a screenshot and save it as `Task 4.png`.

![Task 4](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%204/Tasks/Task%204.png?raw=true)

## ***Task 5 - Create a pie chart***  

The second chart must show **category-wise total sales**.  

To create it:  

1. Click **Insert**.  
2. Select **Pie chart**.  
3. Place the chart on the report canvas.  
4. In the chart setup panel, configure the chart as follows:  

| Setting | Suggested value |
|---|---|
| Chart type | Pie chart |
| Dimension | Category |
| Metric | Total Sales / Sales / Amount |
| Aggregation | SUM |
| Sort | Total Sales descending |

This pie chart should show how much each product category contributes to total sales.  

If the chart shows too many categories, you may keep the default grouping or let Looker Studio group smaller values into `Others`, if available.  

You can now take a screenshot and save it as `Task 5.png`.

![Task 5](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%204/Tasks/Task%205.png?raw=true)

## ***Task 6 - Create a bar chart***  

The third chart must show **quarterly sales of mobile phones**.  

To create it:  

1. Click **Insert**.  
2. Select **Bar chart**.  
3. Place the chart on the report canvas.  
4. In the chart setup panel, configure the chart as follows:  

| Setting | Suggested value |
|---|---|
| Chart type | Bar chart |
| Dimension | Quarter |
| Metric | Total Sales / Sales / Amount |
| Aggregation | SUM |
| Filter | Product category/type = Mobile Phone |
| Sort | Quarter ascending |

To filter only mobile phones:  

1. In the chart setup panel, click **Add a filter**.  
2. Create a filter named `Mobile Phones`.  
3. Include records where the category, product type, or product field equals `Mobile Phone`, `Mobile Phones`, `mobile phone`, or the exact mobile-phone value used in your dataset.  
4. Apply the filter to the bar chart.  

The final result should show one bar for each quarter, usually Q1, Q2, Q3, and Q4, with the total sales of mobile phones for each quarter.  

You can now take a screenshot and save it as `Task 6`.

![Task 6](https://github.com/MatteoMel1985/Data-Engineering-Capstone-Project_IBM_Data_Engineering/blob/main/Module%204/Tasks/Task%206.png?raw=true)
