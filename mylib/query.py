"""Query the database"""

import sqlite3


def query(query_statement):
    """Executes Passed Query"""
    conn = sqlite3.connect("GroceryDB.db")
    cursor = conn.cursor()
    cursor.execute(query_statement)
    print(cursor.fetchall())
    conn.close()
    return "Success"
