
import unittest

from lib.init_db import DbConnector
from sqlalchemy.sql import text

class TestPageParser(unittest.TestCase):

    def setUp(self) -> None:
        self.db_conn = DbConnector()

    def test_load_postion_data(self):
        test_query = """SELECT COUNT(*) 
        FROM position_data;"""

        total_count = self.db_conn.get_connection().execute(text(test_query)).fetchall()[0][0]

        true_count = 43247

        self.assertEqual(total_count, true_count, f"{true_count-total_count} row(s) missing")

    def test_load_ship_engines_data(self):
        test_query = """SELECT engine1_id 
        FROM ship_engines 
        WHERE SHIP_ID = 'Ship_337' ;"""

        test_output = self.db_conn.get_connection().execute(text(test_query)).fetchall()[0][0]

        true_output = "RNX0003702"

        self.assertEqual(test_output, true_output)

    def test_load_ship_owners_data(self):
        test_query = """SELECT COUNT(DISTINCT SHIP_ID) 
        FROM ship_owner 
        WHERE owner = 'viking' 
        GROUP BY owner;"""

        test_output = self.db_conn.get_connection().execute(text(test_query)).fetchall()[0][0]

        true_output = 4

        self.assertEqual(test_output, true_output)



if __name__ == "__main__":
    unittest.main()
