import sys
import os
import unittest

sys.path.append("..")

from get_lines.get_lines import get_lines

class TestGet_Lines(unittest.TestCase):

    def test_get_lines(self):
        """
        Unit test for get_lines().
        """
        
        self.assertEqual(get_lines("test_20191206_1140000.txt", os.getcwd()),
                         299,
                         "Should be equal number of lines.")

if __name__ == "__main__":
    unittest.main()

