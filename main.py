from databricks import sql
from dotenv import load_dotenv
import os

query = """SELECT t1.Player, t1.FG - t2.FG AS FG_Change 
FROM nba__stats_2019 as t1 JOIN heat_2018 as t2 ON t1.Player = t2.Name
WHERE t1.Tm LIKE 'MIA'
ORDER BY FG_Change DESC"""

load_dotenv()

with sql.connect(
    server_hostname=os.getenv("databricks_hostname"),
    http_path=os.getenv("databricks_http"),
    access_token=os.getenv("databricks_access"),
) as connection:
    with connection.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
