![Skills_Network](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/images/image.png)  

<h1 align="center">Resolution Guide: Dashboard Creation with Google Looker Studio</h1>  

# ***Scenario***  

You are a data engineer at an e-commerce company. The company has already completed the setup of its data warehouse, and now you have been asked to build a reporting dashboard that shows the most important sales metrics of the business.  

In this module, you will use **Google Looker Studio** to load the provided `ecommerce.csv` file, inspect the data, create a data source, and build three dashboard visualisations:  

* a line chart showing month-wise total sales for 2020;  
* a pie chart showing category-wise total sales;  
* a bar chart showing quarterly sales of mobile phones.  

# ***Objectives***  

In this assignment you will:  

* upload a CSV file into Google Looker Studio;  
* inspect the first rows of the dataset;  
* create a Looker Studio data source;  
* create a dashboard using line, pie, and bar charts;  
* take screenshots of each required task for peer review or graded submission.  

# ***Tools / Software***  

* Google Looker Studio  
* A Google account  
* The file `ecommerce.csv`  
* A screenshot tool, such as `Alt + Print Screen`, `Windows + Shift + S`, or any other screen capture utility  

# ***Important note about screenshots***  

After each task, take a screenshot and save it with a clear name. A good naming convention is:  

```text
Task 1.png
Task 2.png
Task 3.png
Task 4.png
Task 5.png
Task 6.png
```  

You will probably need these screenshots for the graded quiz or for the final peer-reviewed submission.  

# ***Before you start - Download the dataset***  

Before opening Looker Studio, download the dataset required for this module.  

You can download the CSV file from the link provided in the assignment. The direct file used by the lab is:  

```text
https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0321EN-SkillsNetwork/analytics/ecommerce.csv
```  

Save the file on your local machine as:  

```text
ecommerce.csv
```  

Make sure you know where the file is saved, because you will have to upload it into Google Looker Studio in Task 1.  

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

You can now save the screenshot as:  

```text
Task 1.png
```  

If you later include this guide in your GitHub repository, you can insert the screenshot below:  

```markdown
![Task 1](INSERT_YOUR_IMAGE_URL_HERE)
```  

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

You can now take a screenshot and save it as:  

```text
Task 2.png
```  

If you later include this guide in your GitHub repository, you can insert the screenshot below:  

```markdown
![Task 2](INSERT_YOUR_IMAGE_URL_HERE)
```  

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

You can now save the screenshot as:  

```text
Task 3.png
```  

If you later include this guide in your GitHub repository, you can insert the screenshot below:  

```markdown
![Task 3](INSERT_YOUR_IMAGE_URL_HERE)
```  

# ***Before Exercise 3 - Check or create useful fields***  

Before creating the dashboard charts, it is useful to check whether the dataset already contains the fields needed for the assignment.  

The three charts require the following information:  

| Requirement | Field needed |
|---|---|
| Month-wise total sales for 2020 | Date, Month, Year, Sales or Amount |
| Category-wise total sales | Category, Sales or Amount |
| Quarterly sales of mobile phones | Quarter, Category/Product Type, Sales or Amount |

Depending on how Looker Studio detects the CSV fields, you may already have fields such as `year`, `month`, `quarter`, `category`, and `sales`. If they already exist, use them directly.  

If some fields are missing, you can create calculated fields from the data source.  

For example, if your file has a date field, you can create these calculated fields:  

```text
Year = YEAR(Date)
```  

```text
Month = MONTH(Date)
```  

```text
Quarter = QUARTER(Date)
```  

If the dataset does not have a ready-made sales field, but it has `Quantity` and `Price`, create a calculated field similar to this:  

```text
Total Sales = Quantity * Price
```  

The exact field names may be slightly different in Looker Studio. Therefore, use the names that appear in your uploaded `ecommerce.csv` file. For example, if your date field is called `OrderDate`, use `YEAR(OrderDate)` instead of `YEAR(Date)`.  

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

You can now take a screenshot and save it as:  

```text
Task 4.png
```  

If you later include this guide in your GitHub repository, you can insert the screenshot below:  

```markdown
![Task 4](INSERT_YOUR_IMAGE_URL_HERE)
```  

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

You can now take a screenshot and save it as:  

```text
Task 5.png
```  

If you later include this guide in your GitHub repository, you can insert the screenshot below:  

```markdown
![Task 5](INSERT_YOUR_IMAGE_URL_HERE)
```  

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

You can now take a screenshot and save it as:  

```text
Task 6.png
```  

If you later include this guide in your GitHub repository, you can insert the screenshot below:  

```markdown
![Task 6](INSERT_YOUR_IMAGE_URL_HERE)
```  

# ***Final checklist***  

Before submitting the assignment, make sure you have all required screenshots:  

| Task | Required evidence | Suggested file name |
|---|---|---|
| Task 1 | Successful loading of `ecommerce.csv` | `Task 1.png` |
| Task 2 | First 10 rows of the table | `Task 2.png` |
| Task 3 | Data source created in Looker Studio | `Task 3.png` |
| Task 4 | Line chart of month-wise total sales for 2020 | `Task 4.png` |
| Task 5 | Pie chart of category-wise total sales | `Task 5.png` |
| Task 6 | Bar chart of quarterly sales of mobile phones | `Task 6.png` |

# ***Common issues and corrections***  

## ***The CSV file does not upload***  

If the CSV file does not upload, check that:  

* the file is actually saved as `ecommerce.csv`;  
* the file was not downloaded as an HTML page by mistake;  
* you are using the **File Upload** connector;  
* your Google account has permission to use Looker Studio.  

## ***The date field is not recognised as a date***  

If Looker Studio imports the date as text, open the data source schema and change the field type to **Date**.  

If the date format is not recognised automatically, check the format used in the CSV file and select the appropriate date type in the field settings.  

## ***The sales metric is not summed correctly***  

If sales are not displayed correctly, check the metric aggregation. It should usually be set to **SUM**, not **COUNT**.  

If you only have price and quantity, create this calculated field:  

```text
Total Sales = Quantity * Price
```  

Then use `Total Sales` as the metric and set its aggregation to **SUM**.  

## ***The mobile phone bar chart shows all products***  

If the bar chart shows all products instead of only mobile phones, the filter was probably not applied correctly.  

Open the chart setup panel and verify that the filter includes only the mobile phone category or product type. Use the exact spelling found in the dataset.  

For example, the value might be:  

```text
mobile phone
```  

or:  

```text
Mobile Phones
```  

or:  

```text
Cell Phone
```  

Use whichever value appears in your actual `ecommerce.csv` file.  

# ***End of assignment***  

Once all six screenshots have been saved, the Module 4 assignment is complete.  

# Author  
# ***[Matteo Meloni](https://www.linkedin.com/in/matteo-meloni-40a357154/)***
