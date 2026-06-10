![Skills_Network](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/images/image.png)  

<h1 align="center">Resolution Guide: Dashboard Creation with IBM Cognos Analytics</h1>  

# ***Scenario***  

You are a data engineer at an e-commerce company. The company has already completed the setup of its data warehouse, and now you have been asked to build a reporting dashboard that shows the most important sales metrics of the business.  

In this module, you will use **IBM Cognos Analytics** to load the provided `ecommerce.csv` file, convert it into a Data module, inspect the first rows of the data, create or access the data source, and build three dashboard visualisations:  

* a line chart showing month-wise total sales for 2020;  
* a pie chart showing category-wise total sales;  
* a bar chart showing quarterly sales of mobile phones.  

# ***Objectives***  

In this assignment you will:  

* upload a CSV file into IBM Cognos Analytics;  
* convert the uploaded dataset into a Data module;  
* inspect the first 10 rows of the dataset;  
* verify that the data source exists in the Cognos Analytics workspace;  
* create a dashboard using line, pie, and bar charts;  
* take screenshots of each required task for peer review or graded submission.  

# ***Tools / Software***  

* IBM Cognos Analytics Trial version  
* The file `ecommerce.csv`  
* A screenshot tool, such as `Alt + Print Screen`, `Windows + Shift + S`, or any other screen capture utility  

# ***Important note about screenshots***  

During the assignment, you will be asked to take screenshots and save them on your local machine. These screenshots are usually required either for quiz questions or for the final peer-reviewed submission.  

A good naming convention is:  

```text
Task 1.png
first10rows.jpg
Task 3.png
Task 4.png
Task 5.png
Task 6.png
```  

For **Task 2**, the official instruction specifically says to name the screenshot:  

```text
first10rows.jpg
```  

However, the assignment also says that images may be saved either as `.jpg` or `.png`. Therefore, if your system saves it as `first10rows.png`, it should normally be acceptable as long as the screenshot clearly shows the first 10 rows.  

# ***Before you start - Download the dataset***  

Before opening IBM Cognos Analytics, download the dataset required for this module.  

You can download the CSV file from the link provided in the assignment. The file used by the lab is:  

```text
ecommerce.csv
```  

Save the file somewhere easy to find, for example in your `Downloads` folder or on your Desktop.  

Make sure that:  

* the file is saved as a CSV file;  
* the file name is `ecommerce.csv`;  
* you remember the folder where it was downloaded, because you will have to upload it into Cognos Analytics.  

# ***Exercise 1 - Load data into the data warehouse***  

In this first exercise, we have to load the file `ecommerce.csv` directly into IBM Cognos Analytics.  

## ***Task 1 - Import data***  

Open **IBM Cognos Analytics** in your browser.  

Then proceed as follows:  

1. From the Cognos Analytics home page, click **New**.  
2. Select **Upload files** or **Data** / **Upload data**, depending on the version of Cognos shown in your browser.  
3. Browse your local computer and select the file `ecommerce.csv`.  
4. Wait until Cognos finishes uploading and processing the file.  
5. Once the upload is successful, Cognos should show the dataset inside your workspace, usually under **My content** or **Recent**.  
6. Take a screenshot showing that `ecommerce.csv` has been successfully uploaded into Cognos Analytics.  

The screenshot for this task should clearly show the uploaded file or the successful upload message.  

You can now save the screenshot as:  

```text
Task 1.png
```  

If you later include this guide in your GitHub repository, you can insert the screenshot below:  

```markdown
![Task 1](INSERT_YOUR_IMAGE_URL_HERE)
```  

# ***Task 2 - List first 10 rows***  

The second task asks us to convert the uploaded dataset `ecommerce.csv` into a **Data module** and then take a screenshot of the first 10 rows of the table.  

To do so:  

1. Locate the uploaded file `ecommerce.csv` in **My content** or in the Cognos Analytics workspace.  
2. Click the three dots or context menu beside the file.  
3. Choose **Create data module**.  
4. When Cognos opens the Data module interface, select the table generated from `ecommerce.csv`.  
5. Open the data preview. This is usually available by clicking the table, expanding it, or choosing an option similar to **View data** or **Grid view**.  
6. Make sure that the preview shows the rows of the dataset.  
7. Take a screenshot showing the first 10 rows.  

The official instruction asks us to name this screenshot:  

```text
first10rows.jpg
```  

The screenshot should show the table preview, including the column names and the first rows of the dataset.  

If Cognos shows more than 10 rows, that is not necessarily a problem. The important point is that the first 10 rows are visible in the screenshot.  

If you later include this guide in your GitHub repository, you can insert the screenshot below:  

```markdown
![Task 2](INSERT_YOUR_IMAGE_URL_HERE)
```  

# ***Exercise 2 - Accessing the Data Source in Cognos***  

## ***Task 3 - Create a data source***  

In this task, we have to take a screenshot of the data source created in the Cognos Analytics workspace.  

After uploading `ecommerce.csv` and converting it into a Data module, the dataset should be available as a source inside Cognos.  

To capture the required screenshot:  

1. Go back to the Cognos Analytics home page or content area.  
2. Open **My content**.  
3. Locate the uploaded `ecommerce.csv` file and/or the Data module created from it.  
4. Open the Data module if needed.  
5. Verify that the columns from the CSV file are visible.  
6. Take a screenshot showing the data source or Data module inside the Cognos workspace.  

You can now save the screenshot as:  

```text
Task 3.png
```  

If you later include this guide in your GitHub repository, you can insert the screenshot below:  

```markdown
![Task 3](INSERT_YOUR_IMAGE_URL_HERE)
```  

# ***Before Exercise 3 - Check the useful fields***  

Before creating the dashboard charts, it is important to understand which fields are needed.  

The three charts require the following information:  

| Requirement | Field needed |
|---|---|
| Month-wise total sales for 2020 | Date, Month, Year, Sales or Amount |
| Category-wise total sales | Category, Sales or Amount |
| Quarterly sales of mobile phones | Quarter, Product category/type, Sales or Amount |

Depending on how Cognos reads `ecommerce.csv`, you may already have fields such as:  

```text
Year
Month
Quarter
Category
Product
Sales
Quantity
Price
```  

The exact names may vary slightly. For this reason, always use the field names that appear in your own Cognos data panel.  

If the dataset already has a field called `Sales`, `Total Sales`, `Revenue`, or `Amount`, use that as the metric.  

If there is no ready-made total sales field, but the dataset contains `Quantity` and `Price`, you may need to create a calculation similar to:  

```text
Total Sales = Quantity * Price
```  

In Cognos, this can usually be done from the Data module or dashboard by creating a **calculated field**. The exact syntax may depend on the field names, but the logic is always the same: multiply quantity by price, then aggregate it using **SUM** in the visualisation.  

# ***Exercise 3 - Create a dashboard***  

In this exercise, we create the three required dashboard visualisations.  

To begin:  

1. From the Cognos Analytics home page, click **New**.  
2. Select **Dashboard**.  
3. Choose a template. A blank dashboard is perfectly fine.  
4. Add the Data module or uploaded dataset based on `ecommerce.csv` as the source.  
5. Use the data panel to drag fields into the visualisations.  

## ***Task 4 - Create a line chart***  

The first chart must show **month-wise total sales for the year 2020**.  

To create it:  

1. Open the dashboard created from the `ecommerce.csv` Data module.  
2. Select a **Line chart** visualisation.  
3. Drag the month field into the horizontal axis or x-axis area.  
4. Drag the sales field into the measure or y-axis area.  
5. Make sure the sales measure is aggregated as **SUM**.  
6. Add a filter for the year **2020**.  
7. Sort the month field in ascending order, so the chart runs from January to December.  

The chart configuration should be approximately:  

| Setting | Suggested value |
|---|---|
| Visualisation | Line chart |
| X-axis / Dimension | Month |
| Y-axis / Measure | Total Sales / Sales / Amount |
| Aggregation | SUM |
| Filter | Year = 2020 |
| Sort | Month ascending |

If Cognos uses a full date field instead of a separate month field, make sure the chart groups or summarises the data by month.  

The final chart should show months on the horizontal axis and total sales on the vertical axis.  

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

1. In the same dashboard, add a new visualisation.  
2. Select **Pie chart**.  
3. Drag the category field into the category/slice field.  
4. Drag the sales field into the measure/size field.  
5. Make sure sales are aggregated as **SUM**.  
6. Sort the chart by total sales if Cognos gives you the option to do so.  

The chart configuration should be approximately:  

| Setting | Suggested value |
|---|---|
| Visualisation | Pie chart |
| Category / Slices | Category |
| Measure | Total Sales / Sales / Amount |
| Aggregation | SUM |
| Sort | Total Sales descending |

This pie chart should show how much each product category contributes to total sales.  

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

1. In the same dashboard, add a new visualisation.  
2. Select **Bar chart**.  
3. Drag the quarter field into the x-axis or category axis.  
4. Drag the sales field into the y-axis or measure area.  
5. Make sure sales are aggregated as **SUM**.  
6. Add a filter so that only mobile phones are included.  
7. Sort the quarter field in ascending order.  

The chart configuration should be approximately:  

| Setting | Suggested value |
|---|---|
| Visualisation | Bar chart |
| X-axis / Dimension | Quarter |
| Y-axis / Measure | Total Sales / Sales / Amount |
| Aggregation | SUM |
| Filter | Product category/type = Mobile Phone |
| Sort | Quarter ascending |

To filter only mobile phones, use the exact value that appears in your dataset. For example, the value might be:  

```text
Mobile Phone
```  

or:  

```text
Mobile Phones
```  

or:  

```text
mobile phone
```  

or:  

```text
smart phone
```  

The important thing is to use the exact spelling that appears in the `ecommerce.csv` field used for products or categories.  

The final result should show one bar for each quarter, with the total sales of mobile phones for that quarter.  

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
| Task 1 | Successful loading of `ecommerce.csv` into Cognos Analytics | `Task 1.png` |
| Task 2 | First 10 rows of the table in the Data module | `first10rows.jpg` |
| Task 3 | Data source or Data module created in Cognos Analytics workspace | `Task 3.png` |
| Task 4 | Line chart of month-wise total sales for 2020 | `Task 4.png` |
| Task 5 | Pie chart of category-wise total sales | `Task 5.png` |
| Task 6 | Bar chart of quarterly sales of mobile phones | `Task 6.png` |

# ***Common issues and corrections***  

## ***The CSV file does not upload***  

If the CSV file does not upload, check that:  

* the file is actually saved as `ecommerce.csv`;  
* the file was not downloaded as an HTML page by mistake;  
* you are using the upload option inside IBM Cognos Analytics;  
* your IBM Cognos trial account is active;  
* the browser did not block the upload or the pop-up window.  

## ***The uploaded CSV does not appear in My content***  

If you uploaded the file but cannot find it:  

1. Go back to the Cognos home page.  
2. Open **My content**.  
3. Search for `ecommerce`.  
4. Check whether the file appears under **Recent**.  
5. If not, upload the file again and verify that the upload completes successfully.  

## ***The Data module does not show the first rows***  

If you cannot see the rows after creating the Data module:  

* open the table inside the Data module;  
* look for **View data**, **Preview**, or **Grid view**;  
* expand the table if only the field names are visible;  
* make sure you are viewing the data table and not only the metadata.  

## ***The date field is not recognised correctly***  

If Cognos imports the date as text, the month, quarter, and year may not work properly.  

In that case:  

1. Open the Data module.  
2. Find the date field.  
3. Check its data type.  
4. Change it to a date type if Cognos allows it.  
5. Recreate or refresh the visualisations.  

If the dataset already contains separate fields for year, month, and quarter, use those fields instead of extracting them from the date.  

## ***The sales metric is counted instead of summed***  

If Cognos displays a count of records instead of total sales, the aggregation is probably wrong.  

Open the visualisation settings and verify that the sales field is being summarised with:  

```text
SUM
```  

not:  

```text
COUNT
```  

If you only have quantity and price, create a calculated field:  

```text
Total Sales = Quantity * Price
```  

Then use `Total Sales` in the chart and aggregate it with **SUM**.  

## ***The line chart shows all years instead of only 2020***  

If the line chart includes all years, the filter was not applied correctly.  

Open the line chart and check that there is a filter similar to:  

```text
Year = 2020
```  

Then refresh the chart and verify that only the monthly sales for 2020 are displayed.  

## ***The mobile phone bar chart shows all products***  

If the bar chart shows all products instead of only mobile phones, the product/category filter is missing or incorrect.  

Open the bar chart and check that the filter includes only the mobile phone value. Use the exact spelling found in the dataset.  

For example, if the dataset says `Mobile Phones`, do not filter for `mobile phone`, because Cognos may treat them as different values.  

# ***End of assignment***  

Once all six screenshots have been saved, the IBM Cognos Analytics part of Module 4 is complete.  

# Author  
# ***[Matteo Meloni](https://www.linkedin.com/in/matteo-meloni-40a357154/)***
