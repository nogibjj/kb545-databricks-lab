# 706 Mini-Lab 6: Python Script Complex SQL Query

This purpose of this lab was to setup Azure Databricks Workspace, where we created a SQL Warehouse to host multiple databases that would be queried upon to execute a complex SQL Query. The purpose of the query was to determine if any Miami Heat players in the 2018-2019 roster improved their average Field Goal (FG) in the 2019-2020 season.

### Tasks Performed

* Created an Azure Databricks Workspace
* Created a Compute Cluster within Databricks
* Setup NBA Statistic Databases in a SQL Warehouse
* Create main.py that SQL Warehouse using login credentials stored in .env file
* Executed Complex SQL Query to retrieve FG differential
* Test SQL Connection

### Query Explanation
```
SELECT t1.Player, t1.FG - t2.FG AS FG_Change FROM nba__stats_2019 as t1 JOIN heat_2018 as t2 ON t1.Player = t2.Name
WHERE t1.Tm LIKE 'MIA'
ORDER BY FG_Change DESC
```

This query first joins two databases. One that stores the player stats for Miami Heat players on the 2018-2019 roster, and a second database that stores the player stats for every NBA player during the 2019-2020 season. It joins these two databases based on a player's full name.

Then, the query creates a new field called FG_Change. This field is the average FG of each player during the 2019-2020 game versus the 2018-2019 game. By this logic, a postive value means the player improved, and a negative value means the player got worse. 

Finally, the output is sorted so that the greater the FG change, the higher the player appears in the output. This is shown below

