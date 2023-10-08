import unittest
from unittest.mock import patch
from io import StringIO
from main import query, run_query


class TestRunQuery(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)
    def test_run_query(self, mock_stdout):
        expected_output = "[(u'Goran Dragic', 0), (u'Josh Richardson', -1), (u'Kelly Olynyk', -2),\
              (u'Wayne Ellington', -3), (u'James Johnson', -4), (u'Justise Winslow', -5), \
                (u'Hassan Whiteside', -6), (u'Dion Waiters', -7), (u'Bam Adebayo', -8), \
                    (u'Tyler Johnson', -9), (u'Derrick Jones Jr.', -10), \
                        (u'Rodney McGruder', -11)]\n"
        run_query(query)
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
