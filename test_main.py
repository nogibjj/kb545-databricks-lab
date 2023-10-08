from databricks import sql
from dotenv import load_dotenv
import os

load_dotenv()


def test_connection():
    assert sql.connect(
        server_hostname=os.getenv("databricks_hostname"),
        http_path=os.getenv("databricks_http"),
        access_token=os.getenv("databricks_access"),
    )
