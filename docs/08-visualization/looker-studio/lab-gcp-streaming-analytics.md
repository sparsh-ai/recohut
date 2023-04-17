# Lab: Streaming Analytics and Dashboards

## Objective

Streaming Data Processing - Streaming Analytics and Dashboards

In this lab, you will perform the following tasks:

-   Connect to a BigQuery data source
-   Create reports and charts to visualize BigQuery data

## Creating a data source in Data Studio

- The Google Data Studio User Interface is accessed from outside of the Google Cloud environment. Open a new browser tab preferably in an incognito window. Navigate to: https://datastudio.google.com.

- On the Reports page, in the Start with a Template section, click the Blank Report template. Enter basic info like country and company and check 'No' to all email, then click continue.

- Again click on Reports page, in the Start with a Template section, click the Blank Report template. This time it will take you to a new page and begin an Untitled Report. The Add data to report panel will load from the bottom of the page.

- In the Google Connectors section, select BigQuery. Click on Authorize.

- Select My Projects. In the Project column, click your project name.

- In the Dataset column, click demos.

- In the Table column, click current_conditions.

- Lastly click Add. Check Don't show me this again and click Add to report.

- Once complete, a simple default tabular report appears. This confirms that you can see your BigQuery data in Data Studio.

![](https://user-images.githubusercontent.com/62965911/214003328-2433ef72-8d15-4571-9864-d6d838e520ed.png)

## Creating a bar chart using a calculated field

- Once you have added the current_conditions data source to the report, the next step is to create a visualization. Begin by creating a bar chart. The bar chart will display the total number of vehicles captured for each highway.

- Delete the pre-populated tabular report. You can do this by simply selecting it and pressing delete.

- Next, from the Add a chart menu select the first Bar chart.

- In the Bar chart properties window, on the Data tab, notice the value for Data Source (current_conditions) and the default values for Dimension and Metric.

- If Dimension is not set to highway, then change Dimension to highway. In the Dimension section, click the existing dimension and in the Dimension picker, select highway.

- In the Metric section, click Add metric and add latitude.

- In the Metric section, mouse over Record Count and click the (x) to remove it.

- To gain insight on vehicle volume you need to add a metric for each vehicle detected.

- In the Metric section, click Add metric and add sensorId.

- A count distinct for this column is automatically created. This metric set as a count distinct does not give you a true sense of traffic volume. Click the CTD text and on the popup window choose Count. Type the name vehicles in the name box. Click in the report space off the popup to close it. The change is saved automatically.

- In the Metric section, mouse over latitude and click the (x) to remove it.

- The Dimension should be set to highway and the Metric should be set to sensorId. Notice the chart below is sorted in descending order by default. The highway with the most vehicles is displayed first.

- To enhance the chart, change the bar labels. In the Bar chart properties window, click the STYLE tab.

- In the Bar chart section, check Show data labels.

- The total number of vehicles is displayed above each bar in the chart.

![](https://user-images.githubusercontent.com/62965911/214003324-3daef285-2a07-4f12-88c9-d024b6fbc8a6.png)

## Creating a chart using a custom query

You may find that it is easier to work with an existing query to produce the desired reports and visualizations in Data Studio. The Custom Query option lets you leverage BigQuery's full query capabilities such as joins, unions, and analytical functions.

Alternatively, you can leverage BigQuery's full query capabilities by creating a view. A view is a virtual table defined by a SQL query. You can query data in a view by adding the dataset containing the view as a data source.

When you specify a SQL query as your BigQuery data source, the results of the query are in table format, which becomes the field definition (schema) for your data source. When you use a custom query as a data source, Data Studio uses your SQL as an inner select statement for each generated query to BigQuery.

- From the Add a chart menu select the first Bar chart.

- In the Bar chart properties window, on the Data tab, notice the value for Data Source (current_conditions) and the default values for Dimension and Metric are the same as the previous chart. In the Data Source section, click the current_conditions data source. At the bottom of the pane choose Add data.

- Under Google Connectors, select BigQuery.

- Select CUSTOM QUERY in the first grouping.

- For Billing Project, select your project.

- Type the following in the Enter custom query window and replace the `<PROJECTID>` with your Project ID:

```sql
SELECT max(speed) as maxspeed, min(speed) as minspeed,
avg(speed) as avgspeed, highway
FROM `<PROJECTID>.demos.current_conditions`
group by highway
```

This query uses max/min/avg functions to give you the corresponding speed for each highway.

- Click ADD.

- When prompted, click ADD TO REPORT.

Note: Data Studio may be unable to determine the appropriate Dimension and Metrics for the chart. This requires you to adjust the graph options.

1.  In the Bar chart properties, on the Data tab, in the Metric section, click Record count.
2.  In the Metric picker, select maxspeed.
3.  In the Metric section, click Add metric.
4.  In the Metric picker, select minspeed.
5.  In the Metric section, click Add metric.
6.  In the Metric picker, select avgspeed.
7.  Remove the metric other than maxspeed, minspeed and avgspeed, if exist.

- Your chart now displays the maximum speed, minimum speed, and average speed for each highway.

- Notice each bar has a default color based on the order the metrics were added to the chart.

- For readability, change the chart styles. In the Bar chart properties, click the Style tab.

- In the Color By section, click on the boxes to select different colors.

![](https://user-images.githubusercontent.com/62965911/214003318-7ce0ee63-dfd8-464b-8a0d-86b844ca59dd.png)

Congratulations!