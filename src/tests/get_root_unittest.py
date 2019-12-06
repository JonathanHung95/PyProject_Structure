import sys
import os
import unittest

sys.path.append("..")

from utils.get_root import get_root

class TestGet_Root(unittest.TestCase):

    def test_get_root(self):
        """
        Unit test for get_root().
        """
        
        self.assertEqual(get_root(),
                         os.path.dirname(os.path.dirname(os.getcwd())),
                         "Should be equal")

if __name__ == "__main__":
    unittest.main()
