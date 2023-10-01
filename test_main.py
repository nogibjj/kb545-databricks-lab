import unittest
import sqlite3


def test_connection(self):
    conn = sqlite3.connect("GroceryDB.db")
    self.assertIsNotNone(conn)
    conn.close()
